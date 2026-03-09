from app.repositories.stadium_repository import get_all_stadiums


def list_stadiums() -> list[dict]:
	return get_all_stadiums()
