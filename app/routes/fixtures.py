from flask import Blueprint, jsonify

from app.services.fixture_service import list_next_fixtures


fixtures_bp = Blueprint("fixtures", __name__)


@fixtures_bp.get("/api/fixtures")
def get_fixtures():
	fixtures = list_next_fixtures()
	return jsonify(fixtures), 200