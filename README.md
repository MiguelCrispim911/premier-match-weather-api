# Premier Match Weather API

## 1) Project Name
Premier Match Weather API

## 2) Short Description
Premier Match Weather API is a Flask-based REST API that provides upcoming Premier League fixtures and weather forecasts for those matches. It also includes a lightweight frontend dashboard for visual exploration.

## 3) Project Objective
The objective is to expose a clear and testable API that combines:
- Local real fixture/stadium data (remaining season fixtures stored in project files)
- External weather forecast data from Open-Meteo

This project demonstrates layered Flask architecture, API integration, caching, and frontend consumption.

## 4) Technologies Used
- Python 3
- Flask
- Requests (Open-Meteo integration)
- Pytest
- HTML/CSS/Vanilla JavaScript (frontend)

## 5) General Project Structure
```text
app/
	clients/          # External API clients (Open-Meteo)
	data/             # Local JSON data (fixtures, stadiums)
	repositories/     # Data access layer
	services/         # Business logic layer
	routes/           # Flask blueprints / HTTP endpoints
	templates/        # HTML templates
	static/           # CSS/JS assets
tests/              # Pytest test suite
README.md
requirements.txt
```

## 6) Prerequisites
- Python 3.11+ (3.13 is used in the current environment)
- `pip`
- PowerShell (examples below are PowerShell-based)

## 7) Step-by-Step Installation
```powershell
# 1) Clone repository
git clone <your-repository-url>
cd premier-match-weather-api

# 2) Create virtual environment
python -m venv .venv
```

## 8) Virtual Environment Activation
```powershell
& ".\.venv\Scripts\Activate.ps1"
```

## 9) Dependency Installation
```powershell
pip install -r requirements.txt
```

## 10) Required Environment Variables
This project works with defaults, but these variables are supported:

- `WEATHER_API_TIMEOUT_SECONDS` (default: `6`)
- `WEATHER_CACHE_SUCCESS_SECONDS` (default: `1800`)
- `WEATHER_CACHE_ERROR_SECONDS` (default: `120`)

PowerShell example:
```powershell
$env:WEATHER_API_TIMEOUT_SECONDS="8"
$env:WEATHER_CACHE_SUCCESS_SECONDS="1200"
$env:WEATHER_CACHE_ERROR_SECONDS="60"
```

## 11) How to Run the Project Locally
```powershell
python -m app.main
```

Local server:
- `http://127.0.0.1:5000`

## 12) Available Endpoints with Examples

### Core endpoints

#### Health
- `GET /health`
```powershell
Invoke-RestMethod "http://127.0.0.1:5000/health"
```

#### Stadiums
- `GET /stadiums`
```powershell
Invoke-RestMethod "http://127.0.0.1:5000/stadiums"
```

#### Fixtures (upcoming)
- `GET /api/fixtures`
```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures"
```

#### Fixtures with weather
- `GET /api/fixtures/weather`
```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/weather"
```

### Additional path-based routes (currently enabled)
These routes were added as optional/extended use cases.

#### Fixture by number
- `GET /api/fixtures/{fixture_number}`
```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/1"
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/3"
```

#### Fixture weather by number
- `GET /api/fixtures/weather/{fixture_number}`
```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/weather/1"
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/weather/3"
```

#### Fixture by stadium and kickoff
- `GET /api/fixtures/stadium/{stadium_name}/kickoff/{kickoff_datetime}`
```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/stadium/Emirates%20Stadium/kickoff/2026-04-11T12:30:00"
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/stadium/Stamford%20Bridge/kickoff/2026-04-12T16:30:00"
```

#### Fixture weather by stadium and kickoff
- `GET /api/fixtures/weather/stadium/{stadium_name}/kickoff/{kickoff_datetime}`
```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/weather/stadium/Emirates%20Stadium/kickoff/2026-04-11T12:30:00"
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/weather/stadium/Stamford%20Bridge/kickoff/2026-04-12T16:30:00"
```

#### Fixtures by team
- `GET /api/fixtures/team/{team_name}`
```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/team/Arsenal"
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/team/Manchester%20United"
```

#### Fixture weather by team
- `GET /api/fixtures/weather/team/{team_name}`
```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/weather/team/Chelsea"
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/weather/team/Tottenham%20Hotspur"
```

#### Fixtures by date
- `GET /api/fixtures/date/{YYYY-MM-DD}`
```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/date/2026-04-11"
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/date/2026-04-18"
```

#### Fixture weather by date
- `GET /api/fixtures/weather/date/{YYYY-MM-DD}`
```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/weather/date/2026-04-11"
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/weather/date/2026-04-18"
```

## 13) How to Use the Frontend
1. Start the app locally.
2. Open your browser at:
	 - `http://127.0.0.1:5000/`
3. The dashboard loads upcoming fixtures and weather cards from `/api/fixtures/weather`.

## 14) How to Run the Tests
Run all tests:
```powershell
pytest -q
```

Verbose mode:
```powershell
pytest -v
```

Current test coverage includes:
- Health endpoint
- Stadiums endpoint
- Fixtures endpoint (core + extended routes)
- Weather endpoint (core + extended routes)
- JSON error handling

## 15) Possible Future Improvements
- Add OpenAPI/Swagger documentation
- Add endpoint versioning (`/api/v1/...`)
- Add request/response schemas with validation
- Introduce persistent cache (e.g., Redis) instead of in-memory only
- Add authentication/authorization if needed
- Add CI pipeline with lint + test + coverage report
- Improve timezone handling with dedicated timezone data dependency in all environments