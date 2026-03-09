from app.services.fixture_service import list_next_fixtures


def list_fixtures_with_mock_weather() -> list[dict]:
	fixtures = list_next_fixtures()
	mock_weather = {
		"condition": "Cloudy",
		"temperature_c": 12,
		"humidity": 70,
		"wind_kph": 18,
		"precipitation_probability": 25,
	}

	return [{**fixture, "weather": dict(mock_weather)} for fixture in fixtures]
