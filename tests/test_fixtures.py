def test_fixtures_returns_next_20_with_expected_fields(client):
	response = client.get("/api/fixtures")

	assert response.status_code == 200
	assert response.is_json

	data = response.get_json()
	assert isinstance(data, list)
	assert len(data) == 20

	first_fixture = data[0]
	assert set(first_fixture.keys()) == {
		"home_team",
		"away_team",
		"stadium",
		"kickoff_datetime",
	}