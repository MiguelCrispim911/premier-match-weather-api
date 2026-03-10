from datetime import UTC, datetime, timedelta

from app.repositories.fixture_repository import get_all_fixtures
from app.repositories.stadium_repository import get_all_stadiums


def _last_sunday_day(year: int, month: int) -> int:
	for day in range(31, 24, -1):
		candidate = datetime(year, month, day)
		if candidate.weekday() == 6:
			return day

	return 31


def _is_london_bst(local_datetime: datetime) -> bool:
	year = local_datetime.year
	bst_start_day = _last_sunday_day(year, 3)
	bst_end_day = _last_sunday_day(year, 10)

	bst_start = datetime(year, 3, bst_start_day, 1, 0, 0)
	bst_end = datetime(year, 10, bst_end_day, 2, 0, 0)
	return bst_start <= local_datetime < bst_end


def _london_offset_for_local_datetime(local_datetime: datetime) -> timedelta:
	return timedelta(hours=1 if _is_london_bst(local_datetime) else 0)


def _to_utc_assuming_london(local_datetime: datetime) -> datetime:
	offset = _london_offset_for_local_datetime(local_datetime)
	return (local_datetime - offset).replace(tzinfo=UTC)


def _parse_kickoff_datetime(value: str | None) -> datetime | None:
	if not isinstance(value, str):
		return None

	try:
		parsed = datetime.fromisoformat(value)
	except ValueError:
		return None

	if parsed.tzinfo is None:
		return _to_utc_assuming_london(parsed)

	return parsed.astimezone(UTC)


def list_next_fixtures(limit: int = 20) -> list[dict]:
	fixtures = get_all_fixtures()
	stadiums = get_all_stadiums()
	stadium_name_by_id = {stadium.get("id"): stadium.get("name") for stadium in stadiums}
	now = datetime.now(UTC)

	normalized_fixtures: list[tuple[datetime, dict]] = []

	for fixture in fixtures:
		kickoff_datetime_raw = fixture.get("kickoff_datetime")
		kickoff_datetime = _parse_kickoff_datetime(kickoff_datetime_raw)
		if kickoff_datetime is None or kickoff_datetime < now:
			continue

		stadium_id = fixture.get("stadium_id")
		normalized_fixtures.append(
			(
				kickoff_datetime,
				{
					"home_team": fixture.get("home_team"),
					"away_team": fixture.get("away_team"),
					"stadium": stadium_name_by_id.get(stadium_id, stadium_id),
					"kickoff_datetime": kickoff_datetime_raw,
				},
			)
		)

	normalized_fixtures.sort(key=lambda item: item[0])
	return [fixture for _, fixture in normalized_fixtures[:limit]]