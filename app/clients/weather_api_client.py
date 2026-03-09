from datetime import datetime

import requests

from app.config import WEATHER_API_TIMEOUT_SECONDS


OPEN_METEO_FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
DEFAULT_TIMEOUT_SECONDS = WEATHER_API_TIMEOUT_SECONDS


def get_hourly_forecast_for_kickoff(
	latitude: float,
	longitude: float,
	kickoff_datetime: datetime,
	timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
) -> dict | None:
	params = {
		"latitude": latitude,
		"longitude": longitude,
		"hourly": "weather_code,temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation_probability",
		"start_date": kickoff_datetime.date().isoformat(),
		"end_date": kickoff_datetime.date().isoformat(),
		"timezone": "Europe/London",
	}

	try:
		response = requests.get(OPEN_METEO_FORECAST_URL, params=params, timeout=timeout_seconds)
		response.raise_for_status()
	except requests.Timeout:
		return None
	except requests.RequestException:
		return None

	payload = response.json()
	if not isinstance(payload, dict):
		return None

	hourly_data = payload.get("hourly")
	if not isinstance(hourly_data, dict):
		return None

	return hourly_data
