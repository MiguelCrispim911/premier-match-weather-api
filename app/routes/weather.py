from flask import Blueprint, abort, jsonify

from app.services.weather_service import list_fixtures_with_mock_weather


weather_bp = Blueprint("weather", __name__)


@weather_bp.get("/api/fixtures/weather")
def get_fixtures_weather():
	fixtures_with_weather = list_fixtures_with_mock_weather()
	return jsonify(fixtures_with_weather), 200


# BEGIN OPTIONAL PATH-ENDPOINTS (remove this block if you don't want it)
@weather_bp.get("/api/fixtures/weather/<int:fixture_number>")
def get_fixture_weather_by_number(fixture_number: int):
	fixtures_with_weather = list_fixtures_with_mock_weather()

	if fixture_number < 1 or fixture_number > len(fixtures_with_weather):
		abort(404, description="Fixture weather not found for the requested number.")

	return jsonify(fixtures_with_weather[fixture_number - 1]), 200


@weather_bp.get("/api/fixtures/weather/stadium/<path:stadium_name>/kickoff/<path:kickoff_datetime>")
def get_fixture_weather_by_stadium_and_kickoff(stadium_name: str, kickoff_datetime: str):
	fixtures_with_weather = list_fixtures_with_mock_weather()

	for fixture in fixtures_with_weather:
		if (
			str(fixture.get("stadium", "")).strip().lower() == stadium_name.strip().lower()
			and fixture.get("kickoff_datetime") == kickoff_datetime
		):
			return jsonify(fixture), 200

	abort(404, description="Fixture weather not found for the requested stadium and kickoff.")


@weather_bp.get("/api/fixtures/weather/team/<path:team_name>")
def get_fixtures_weather_by_team(team_name: str):
	fixtures_with_weather = list_fixtures_with_mock_weather()
	team_name_normalized = team_name.strip().lower()

	matching_fixtures = [
		fixture
		for fixture in fixtures_with_weather
		if str(fixture.get("home_team", "")).strip().lower() == team_name_normalized
		or str(fixture.get("away_team", "")).strip().lower() == team_name_normalized
	]

	if not matching_fixtures:
		abort(404, description="No fixture weather found for the requested team.")

	return jsonify(matching_fixtures), 200


@weather_bp.get("/api/fixtures/weather/date/<path:kickoff_date>")
def get_fixtures_weather_by_date(kickoff_date: str):
	fixtures_with_weather = list_fixtures_with_mock_weather()
	matching_fixtures = [
		fixture
		for fixture in fixtures_with_weather
		if str(fixture.get("kickoff_datetime", "")).startswith(kickoff_date)
	]

	if not matching_fixtures:
		abort(404, description="No fixture weather found for the requested date.")

	return jsonify(matching_fixtures), 200


# END OPTIONAL PATH-ENDPOINTS
