def test_not_found_returns_json_error(client):
	response = client.get("/api/unknown-endpoint")

	assert response.status_code == 404
	assert response.is_json

	data = response.get_json()
	assert isinstance(data, dict)
	assert "error" in data
	assert data["error"]["code"] == 404
	assert "message" in data["error"]