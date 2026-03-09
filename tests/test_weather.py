from app.services import weather_service


def test_fixtures_weather_returns_expected_structure(client, monkeypatch):
	def fake_hourly_forecast(*args, **kwargs):
		return {
			"time": ["2026-03-14T15:00"],
			"weather_code": [3],
			"temperature_2m": [12.0],
			"relative_humidity_2m": [70],
			"wind_speed_10m": [18.0],
			"precipitation_probability": [25],
		}

	monkeypatch.setattr(weather_service, "get_hourly_forecast_for_kickoff", fake_hourly_forecast)

	response = client.get("/api/fixtures/weather")

	assert response.status_code == 200
	assert response.is_json

	data = response.get_json()
	assert isinstance(data, list)
	assert len(data) == 20

	first_item = data[0]
	assert set(first_item.keys()) == {
		"home_team",
		"away_team",
		"stadium",
		"kickoff_datetime",
		"weather",
	}

	weather = first_item["weather"]
	assert isinstance(weather, dict)
	assert set(weather.keys()) == {
		"condition",
		"temperature_c",
		"humidity",
		"wind_kph",
		"precipitation_probability",
	}
