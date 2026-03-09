const API_ENDPOINT = "/api/fixtures/weather";

const placeholderMatches = [
	{
		home_team: "Arsenal",
		away_team: "Chelsea",
		stadium: "Emirates Stadium",
		kickoff: "2026-03-14 12:30",
		weather_icon: "sun",
		temperature_c: 16,
		humidity_percent: 54,
		wind_speed_kmh: 12,
		precipitation_probability_percent: 10,
	},
	{
		home_team: "Liverpool",
		away_team: "Tottenham",
		stadium: "Anfield",
		kickoff: "2026-03-14 15:00",
		weather_icon: "clouds",
		temperature_c: 13,
		humidity_percent: 62,
		wind_speed_kmh: 14,
		precipitation_probability_percent: 22,
	},
	{
		home_team: "Manchester City",
		away_team: "Newcastle",
		stadium: "Etihad Stadium",
		kickoff: "2026-03-14 17:30",
		weather_icon: "rain",
		temperature_c: 11,
		humidity_percent: 76,
		wind_speed_kmh: 18,
		precipitation_probability_percent: 68,
	},
	{
		home_team: "Aston Villa",
		away_team: "Brighton",
		stadium: "Villa Park",
		kickoff: "2026-03-15 12:00",
		weather_icon: "clouds",
		temperature_c: 12,
		humidity_percent: 64,
		wind_speed_kmh: 13,
		precipitation_probability_percent: 30,
	},
	{
		home_team: "West Ham",
		away_team: "Brentford",
		stadium: "London Stadium",
		kickoff: "2026-03-15 14:00",
		weather_icon: "rain",
		temperature_c: 10,
		humidity_percent: 80,
		wind_speed_kmh: 20,
		precipitation_probability_percent: 72,
	},
	{
		home_team: "Everton",
		away_team: "Leicester",
		stadium: "Goodison Park",
		kickoff: "2026-03-15 16:30",
		weather_icon: "sun",
		temperature_c: 14,
		humidity_percent: 58,
		wind_speed_kmh: 11,
		precipitation_probability_percent: 12,
	},
	{
		home_team: "Manchester United",
		away_team: "Wolves",
		stadium: "Old Trafford",
		kickoff: "2026-03-16 20:00",
		weather_icon: "clouds",
		temperature_c: 9,
		humidity_percent: 70,
		wind_speed_kmh: 17,
		precipitation_probability_percent: 34,
	},
	{
		home_team: "Fulham",
		away_team: "Crystal Palace",
		stadium: "Craven Cottage",
		kickoff: "2026-03-17 19:45",
		weather_icon: "rain",
		temperature_c: 8,
		humidity_percent: 82,
		wind_speed_kmh: 19,
		precipitation_probability_percent: 66,
	},
	{
		home_team: "Nottingham Forest",
		away_team: "Bournemouth",
		stadium: "City Ground",
		kickoff: "2026-03-18 20:00",
		weather_icon: "clouds",
		temperature_c: 11,
		humidity_percent: 67,
		wind_speed_kmh: 15,
		precipitation_probability_percent: 28,
	},
	{
		home_team: "Burnley",
		away_team: "Southampton",
		stadium: "Turf Moor",
		kickoff: "2026-03-19 20:00",
		weather_icon: "sun",
		temperature_c: 12,
		humidity_percent: 56,
		wind_speed_kmh: 10,
		precipitation_probability_percent: 9,
	},
];

const weatherIconMap = {
	sun: "☀️",
	clouds: "☁️",
	rain: "🌧️",
};

function createMatchCard(match) {
	const icon = weatherIconMap[match.weather_icon] || "☁️";

	return `
		<article class="match-card">
			<div class="match-header">
				<h2 class="teams">${match.home_team} vs ${match.away_team}</h2>
				<span class="weather-icon" aria-label="weather icon">${icon}</span>
			</div>
			<p class="meta">Stadium: ${match.stadium}</p>
			<p class="meta">Kickoff: ${match.kickoff}</p>
			<ul class="stats">
				<li class="stat-item">Temp: ${match.temperature_c}°C</li>
				<li class="stat-item">Humidity: ${match.humidity_percent}%</li>
				<li class="stat-item">Wind: ${match.wind_speed_kmh} km/h</li>
				<li class="stat-item">Precip: ${match.precipitation_probability_percent}%</li>
			</ul>
		</article>
	`;
}

function renderMatches(matches) {
	const grid = document.getElementById("matches-grid");

	if (!grid) {
		return;
	}

	grid.innerHTML = matches.slice(0, 10).map(createMatchCard).join("");
}

async function loadMatches() {
	// Placeholder only for now.
	// Later this function can call the backend endpoint:
	// const response = await fetch(API_ENDPOINT);
	// const matches = await response.json();
	renderMatches(placeholderMatches);
}

document.addEventListener("DOMContentLoaded", loadMatches);
