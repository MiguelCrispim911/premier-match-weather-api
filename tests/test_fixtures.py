from datetime import datetime


def test_fixtures_returns_expected_fields_and_max_limit(client):
	response = client.get("/api/fixtures")

	assert response.status_code == 200
	assert response.is_json

	data = response.get_json()
	assert isinstance(data, list)
	assert 0 < len(data) <= 20

	first_fixture = data[0]
	assert set(first_fixture.keys()) == {
		"home_team",
		"away_team",
		"stadium",
		"kickoff_datetime",
	}


def test_fixtures_are_sorted_by_kickoff_datetime(client):
	response = client.get("/api/fixtures")
	assert response.status_code == 200

	data = response.get_json()
	kickoffs = [datetime.fromisoformat(item["kickoff_datetime"]) for item in data]
	assert kickoffs == sorted(kickoffs)


def test_fixture_by_number_matches_list_position(client):
	all_response = client.get("/api/fixtures")
	all_data = all_response.get_json()

	one_response = client.get("/api/fixtures/1")
	assert one_response.status_code == 200
	assert one_response.is_json

	assert one_response.get_json() == all_data[0]


def test_fixture_by_number_not_found_returns_json_error(client):
	response = client.get("/api/fixtures/9999")
	assert response.status_code == 404
	assert response.is_json
	assert response.get_json()["error"]["code"] == 404


def test_fixtures_by_team_returns_only_requested_team_matches(client):
	response = client.get("/api/fixtures/team/Arsenal")
	assert response.status_code == 200
	assert response.is_json

	data = response.get_json()
	assert isinstance(data, list)
	assert len(data) > 0

	for fixture in data:
		home_team = str(fixture.get("home_team", "")).lower()
		away_team = str(fixture.get("away_team", "")).lower()
		assert "arsenal" in {home_team, away_team}


def test_fixtures_by_team_not_found_returns_json_error(client):
	response = client.get("/api/fixtures/team/EquipoInexistente123")
	assert response.status_code == 404
	assert response.is_json
	assert response.get_json()["error"]["code"] == 404


def test_fixtures_by_date_returns_only_requested_date(client):
	all_response = client.get("/api/fixtures")
	all_data = all_response.get_json()
	assert len(all_data) > 0

	target_date = all_data[0]["kickoff_datetime"].split("T")[0]
	response = client.get(f"/api/fixtures/date/{target_date}")
	assert response.status_code == 200
	assert response.is_json

	data = response.get_json()
	assert len(data) > 0
	for fixture in data:
		assert str(fixture.get("kickoff_datetime", "")).startswith(target_date)


def test_fixtures_by_date_not_found_returns_json_error(client):
	response = client.get("/api/fixtures/date/2099-12-31")
	assert response.status_code == 404
	assert response.is_json
	assert response.get_json()["error"]["code"] == 404