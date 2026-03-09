from app.repositories.fixture_repository import get_all_fixtures
from app.repositories.stadium_repository import get_all_stadiums


def list_next_fixtures(limit: int = 20) -> list[dict]:
	fixtures = get_all_fixtures()
	stadiums = get_all_stadiums()
	stadium_name_by_id = {stadium.get("id"): stadium.get("name") for stadium in stadiums}

	normalized_fixtures = []

	for fixture in fixtures:
		stadium_id = fixture.get("stadium_id")
		normalized_fixtures.append(
			{
				"home_team": fixture.get("home_team"),
				"away_team": fixture.get("away_team"),
				"stadium": stadium_name_by_id.get(stadium_id, stadium_id),
				"kickoff_datetime": fixture.get("kickoff_datetime"),
			}
		)

	return normalized_fixtures[:limit]