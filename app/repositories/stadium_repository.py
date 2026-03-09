import json
from pathlib import Path


def get_all_stadiums() -> list[dict]:
	data_path = Path(__file__).resolve().parents[1] / "data" / "stadiums.json"

	with data_path.open("r", encoding="utf-8") as file:
		stadiums = json.load(file)

	if isinstance(stadiums, list):
		return stadiums

	return []
