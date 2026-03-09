from datetime import UTC, datetime, timedelta

from app.config import WEATHER_CACHE_ERROR_SECONDS, WEATHER_CACHE_SUCCESS_SECONDS
from app.clients.weather_api_client import get_hourly_forecast_for_kickoff
from app.repositories.stadium_repository import get_all_stadiums
from app.services.fixture_service import list_next_fixtures


_FORECAST_CACHE: dict[tuple[float, float, str], tuple[datetime, dict | None]] = {}
_SUCCESS_CACHE_TTL = timedelta(seconds=WEATHER_CACHE_SUCCESS_SECONDS)
_ERROR_CACHE_TTL = timedelta(seconds=WEATHER_CACHE_ERROR_SECONDS)


def _cache_key(latitude: float, longitude: float, kickoff_datetime: datetime) -> tuple[float, float, str]:
	return (round(latitude, 4), round(longitude, 4), kickoff_datetime.date().isoformat())


def _utc_now() -> datetime:
	return datetime.now(UTC)


def _get_hourly_forecast_cached(
	latitude: float,
	longitude: float,
	kickoff_datetime: datetime,
) -> dict | None:
	key = _cache_key(latitude, longitude, kickoff_datetime)
	now = _utc_now()
	cached = _FORECAST_CACHE.get(key)

	if cached:
		expires_at, cached_hourly = cached
		if now < expires_at:
			return cached_hourly

	hourly_data = get_hourly_forecast_for_kickoff(
		latitude=latitude,
		longitude=longitude,
		kickoff_datetime=kickoff_datetime,
	)

	ttl = _SUCCESS_CACHE_TTL if hourly_data is not None else _ERROR_CACHE_TTL
	_FORECAST_CACHE[key] = (now + ttl, hourly_data)
	return hourly_data


def _fallback_weather() -> dict:
	return {
		"condition": "Unknown",
		"temperature_c": None,
		"humidity": None,
		"wind_kph": None,
		"precipitation_probability": None,
	}


def _condition_from_weather_code(weather_code: int | None) -> str:
	if weather_code is None:
		return "Unknown"

	if weather_code == 0:
		return "Clear"
	if weather_code in {1, 2, 3}:
		return "Cloudy"
	if weather_code in {45, 48}:
		return "Fog"
	if weather_code in {51, 53, 55, 56, 57}:
		return "Drizzle"
	if weather_code in {61, 63, 65, 66, 67, 80, 81, 82}:
		return "Rain"
	if weather_code in {71, 73, 75, 77, 85, 86}:
		return "Snow"
	if weather_code in {95, 96, 99}:
		return "Thunderstorm"

	return "Unknown"


def _value_at(values: list, index: int):
	if not isinstance(values, list):
		return None
	if index < 0 or index >= len(values):
		return None
	return values[index]


def _normalize_weather_from_hourly(hourly_data: dict, kickoff_datetime: datetime) -> dict:
	times = hourly_data.get("time")
	if not isinstance(times, list) or not times:
		return _fallback_weather()

	closest_index = -1
	closest_delta_seconds = None

	for index, time_value in enumerate(times):
		if not isinstance(time_value, str):
			continue

		try:
			forecast_datetime = datetime.fromisoformat(time_value)
		except ValueError:
			continue

		delta_seconds = abs((forecast_datetime - kickoff_datetime).total_seconds())
		if closest_delta_seconds is None or delta_seconds < closest_delta_seconds:
			closest_delta_seconds = delta_seconds
			closest_index = index

	if closest_index < 0:
		return _fallback_weather()

	weather_code = _value_at(hourly_data.get("weather_code"), closest_index)
	temperature = _value_at(hourly_data.get("temperature_2m"), closest_index)
	humidity = _value_at(hourly_data.get("relative_humidity_2m"), closest_index)
	wind_speed = _value_at(hourly_data.get("wind_speed_10m"), closest_index)
	precipitation_probability = _value_at(
		hourly_data.get("precipitation_probability"),
		closest_index,
	)

	return {
		"condition": _condition_from_weather_code(weather_code if isinstance(weather_code, int) else None),
		"temperature_c": temperature,
		"humidity": humidity,
		"wind_kph": wind_speed,
		"precipitation_probability": precipitation_probability,
	}


def list_fixtures_with_mock_weather() -> list[dict]:
	fixtures = list_next_fixtures()
	stadiums = get_all_stadiums()
	stadium_coordinates = {
		stadium.get("name"): (stadium.get("latitude"), stadium.get("longitude"))
		for stadium in stadiums
	}

	fixtures_with_weather = []

	for fixture in fixtures:
		weather_data = _fallback_weather()
		stadium_name = fixture.get("stadium")
		kickoff_raw = fixture.get("kickoff_datetime")

		if isinstance(stadium_name, str) and isinstance(kickoff_raw, str):
			coordinates = stadium_coordinates.get(stadium_name)
			if coordinates:
				latitude, longitude = coordinates
				if isinstance(latitude, (int, float)) and isinstance(longitude, (int, float)):
					try:
						kickoff_datetime = datetime.fromisoformat(kickoff_raw)
					except ValueError:
						kickoff_datetime = None

					if kickoff_datetime is not None:
						hourly_data = _get_hourly_forecast_cached(
							latitude=float(latitude),
							longitude=float(longitude),
							kickoff_datetime=kickoff_datetime,
						)
						if hourly_data is not None:
							weather_data = _normalize_weather_from_hourly(hourly_data, kickoff_datetime)

		fixtures_with_weather.append({**fixture, "weather": weather_data})

	return fixtures_with_weather
