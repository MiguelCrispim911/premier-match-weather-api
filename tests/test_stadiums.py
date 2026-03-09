def test_stadiums_returns_list_and_count(client):
	response = client.get("/stadiums")

	assert response.status_code == 200
	assert response.is_json

	data = response.get_json()
	assert isinstance(data, dict)
	assert set(data.keys()) == {"stadiums", "count"}
	assert isinstance(data["stadiums"], list)
	assert isinstance(data["count"], int)
	assert data["count"] == len(data["stadiums"])

	if data["stadiums"]:
		first_stadium = data["stadiums"][0]
		assert "id" in first_stadium
		assert "name" in first_stadium
