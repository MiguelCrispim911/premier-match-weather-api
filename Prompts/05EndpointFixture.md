Extend the Flask project.

Implement a fixtures endpoint that returns the next 20 Premier League matches.

Endpoint:

GET /api/fixtures

For now do NOT call any external API.

Instead return mock data with the following fields:

- home_team
- away_team
- stadium
- kickoff_datetime

Example response:

[
  {
    "home_team": "Arsenal",
    "away_team": "Chelsea",
    "stadium": "Emirates Stadium",
    "kickoff_datetime": "2026-03-15T16:30:00"
  }
]

Architecture rules:
- routes -> services
- create fixture_service.py
- keep logic outside routes

Return JSON.