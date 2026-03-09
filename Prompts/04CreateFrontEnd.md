Create a simple frontend for the Flask project "Premier Match Weather API".

The homepage should display a dashboard of the next 10 Premier League matches.

IMPORTANT:
Do NOT call any API yet.
Just prepare the UI structure.

Requirements:

The page should show a grid of 10 match cards.

Each card must contain placeholders for:

- home_team vs away_team
- stadium name
- kickoff date and time
- weather condition icon (sun, clouds, rain)
- temperature in °C
- humidity %
- wind speed km/h
- precipitation probability %

Layout:

Use a responsive CSS grid with 4 cards per row.

Each card should look like a modern sports dashboard card.

Files to generate:

templates/index.html
static/css/styles.css
static/js/app.js

The JavaScript file should include placeholder data for 20 matches and render them into the cards.

Do not implement real API calls yet, but structure the code so that later it can call:

GET /api/fixtures/weather

Use vanilla JavaScript only.