Extend the Flask project.

Create a fixtures repository that reads fixture data from:

app/data/fixtures.json

Implement:

GET /api/fixtures

The endpoint should return the next 20 Premier League matches.

Architecture:

routes -> services -> repositories

Do not hardcode fixtures in Python.
Load them from the JSON file instead.

Return JSON.