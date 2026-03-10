import pytest

from app.services import weather_service


@pytest.fixture
def fake_weather_api(monkeypatch):
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
	weather_service._FORECAST_CACHE.clear()


def test_fixtures_weather_returns_expected_structure(client, fake_weather_api):

	response = client.get("/api/fixtures/weather")

	assert response.status_code == 200
	assert response.is_json

	data = response.get_json()
	assert isinstance(data, list)
	assert 0 < len(data) <= 20

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


def test_fixture_weather_by_number_matches_list_position(client, fake_weather_api):
	all_response = client.get("/api/fixtures/weather")
	all_data = all_response.get_json()

	one_response = client.get("/api/fixtures/weather/1")
	assert one_response.status_code == 200
	assert one_response.is_json
	assert one_response.get_json() == all_data[0]


def test_fixture_weather_by_number_not_found_returns_json_error(client, fake_weather_api):
	response = client.get("/api/fixtures/weather/9999")
	assert response.status_code == 404
	assert response.is_json
	assert response.get_json()["error"]["code"] == 404


def test_fixtures_weather_by_team_returns_only_requested_team_matches(client, fake_weather_api):
	response = client.get("/api/fixtures/weather/team/Chelsea")
	assert response.status_code == 200
	assert response.is_json

	data = response.get_json()
	assert len(data) > 0
	for fixture in data:
		home_team = str(fixture.get("home_team", "")).lower()
		away_team = str(fixture.get("away_team", "")).lower()
		assert "chelsea" in {home_team, away_team}
		assert "weather" in fixture


def test_fixtures_weather_by_team_not_found_returns_json_error(client, fake_weather_api):
	response = client.get("/api/fixtures/weather/team/EquipoInexistente123")
	assert response.status_code == 404
	assert response.is_json
	assert response.get_json()["error"]["code"] == 404


def test_fixtures_weather_by_date_returns_only_requested_date(client, fake_weather_api):
	all_response = client.get("/api/fixtures/weather")
	all_data = all_response.get_json()
	target_date = all_data[0]["kickoff_datetime"].split("T")[0]

	response = client.get(f"/api/fixtures/weather/date/{target_date}")
	assert response.status_code == 200
	assert response.is_json

	data = response.get_json()
	assert len(data) > 0
	for fixture in data:
		assert str(fixture.get("kickoff_datetime", "")).startswith(target_date)
		assert "weather" in fixture


def test_fixtures_weather_by_date_not_found_returns_json_error(client, fake_weather_api):
	response = client.get("/api/fixtures/weather/date/2099-12-31")
	assert response.status_code == 404
	assert response.is_json
	assert response.get_json()["error"]["code"] == 404
