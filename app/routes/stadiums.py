from flask import Blueprint, jsonify

from app.services.stadium_service import list_stadiums


stadiums_bp = Blueprint("stadiums", __name__)


@stadiums_bp.get("/stadiums")
def get_stadiums():
	stadiums = list_stadiums()
	return jsonify({"stadiums": stadiums, "count": len(stadiums)}), 200
