import os


def _get_int_env(name: str, default: int) -> int:
	value = os.getenv(name)
	if value is None:
		return default

	try:
		parsed = int(value)
	except ValueError:
		return default

	return parsed if parsed >= 0 else default


WEATHER_API_TIMEOUT_SECONDS = _get_int_env("WEATHER_API_TIMEOUT_SECONDS", 6)
WEATHER_CACHE_SUCCESS_SECONDS = _get_int_env("WEATHER_CACHE_SUCCESS_SECONDS", 1800)
WEATHER_CACHE_ERROR_SECONDS = _get_int_env("WEATHER_CACHE_ERROR_SECONDS", 120)
