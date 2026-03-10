from flask import Blueprint, abort, jsonify

from app.services.fixture_service import list_next_fixtures


fixture_bp = Blueprint("fixture", __name__)


@fixture_bp.get("/api/fixtures")
def get_fixtures():
	fixtures = list_next_fixtures()
	return jsonify(fixtures), 200


# BEGIN OPTIONAL PATH-ENDPOINTS (remove this block if you don't want it)
@fixture_bp.get("/api/fixtures/<int:fixture_number>")
def get_fixture_by_number(fixture_number: int):
	fixtures = list_next_fixtures()

	if fixture_number < 1 or fixture_number > len(fixtures):
		abort(404, description="Fixture not found for the requested number.")

	return jsonify(fixtures[fixture_number - 1]), 200


@fixture_bp.get("/api/fixtures/stadium/<path:stadium_name>/kickoff/<path:kickoff_datetime>")
def get_fixture_by_stadium_and_kickoff(stadium_name: str, kickoff_datetime: str):
	fixtures = list_next_fixtures(limit=500)

	for fixture in fixtures:
		if (
			str(fixture.get("stadium", "")).strip().lower() == stadium_name.strip().lower()
			and fixture.get("kickoff_datetime") == kickoff_datetime
		):
			return jsonify(fixture), 200

	abort(404, description="Fixture not found for the requested stadium and kickoff.")


@fixture_bp.get("/api/fixtures/team/<path:team_name>")
def get_fixtures_by_team(team_name: str):
	fixtures = list_next_fixtures(limit=500)
	team_name_normalized = team_name.strip().lower()

	matching_fixtures = [
		fixture
		for fixture in fixtures
		if str(fixture.get("home_team", "")).strip().lower() == team_name_normalized
		or str(fixture.get("away_team", "")).strip().lower() == team_name_normalized
	]

	if not matching_fixtures:
		abort(404, description="No fixtures found for the requested team.")

	return jsonify(matching_fixtures), 200


@fixture_bp.get("/api/fixtures/date/<path:kickoff_date>")
def get_fixtures_by_date(kickoff_date: str):
	fixtures = list_next_fixtures(limit=500)
	matching_fixtures = [
		fixture
		for fixture in fixtures
		if str(fixture.get("kickoff_datetime", "")).startswith(kickoff_date)
	]

	if not matching_fixtures:
		abort(404, description="No fixtures found for the requested date.")

	return jsonify(matching_fixtures), 200


# END OPTIONAL PATH-ENDPOINTS