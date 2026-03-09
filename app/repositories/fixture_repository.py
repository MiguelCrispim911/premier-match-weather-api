import json
from pathlib import Path


def get_all_fixtures() -> list[dict]:
	data_path = Path(__file__).resolve().parents[1] / "data" / "fixtures.json"

	with data_path.open("r", encoding="utf-8") as file:
		fixtures = json.load(file)

	if isinstance(fixtures, list):
		return fixtures

	return []