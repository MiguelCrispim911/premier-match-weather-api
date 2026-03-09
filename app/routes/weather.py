from flask import Blueprint, jsonify

from app.services.weather_service import list_fixtures_with_mock_weather


weather_bp = Blueprint("weather", __name__)


@weather_bp.get("/api/fixtures/weather")
def get_fixtures_weather():
	fixtures_with_weather = list_fixtures_with_mock_weather()
	return jsonify(fixtures_with_weather), 200
