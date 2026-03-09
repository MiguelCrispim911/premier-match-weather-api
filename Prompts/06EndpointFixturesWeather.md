Extend the Flask API.

Create a new endpoint:

GET /api/fixtures/weather

This endpoint should combine fixture data with mock weather data.

Steps:

1. Get fixtures from fixture_service
2. For each fixture attach mock weather information:

{
 "condition": "Cloudy",
 "temperature_c": 12,
 "humidity": 70,
 "wind_kph": 18,
 "precipitation_probability": 25
}

Return a list like:

[
 {
  "home_team": "...",
  "away_team": "...",
  "stadium": "...",
  "kickoff_datetime": "...",
  "weather": {...}
 }
]

Do NOT call a real weather API yet.
Do not do tests yet.
Keep logic inside services layer.