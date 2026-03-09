from flask import Blueprint, jsonify

from app.services.fixture_service import list_next_fixtures


fixture_bp = Blueprint("fixture", __name__)


@fixture_bp.get("/api/fixtures")
def get_fixtures():
	fixtures = list_next_fixtures()
	return jsonify(fixtures), 200