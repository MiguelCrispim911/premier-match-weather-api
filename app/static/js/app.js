const API_ENDPOINT = "/api/fixtures/weather";

const fallbackMatches = [];

const weatherIconMap = {
	sunny: "☀️",
	clear: "☀️",
	cloudy: "☁️",
	overcast: "☁️",
	fog: "🌫️",
	drizzle: "🌦️",
	rain: "🌧️",
	rainy: "🌧️",
	snow: "❄️",
	thunderstorm: "⛈️",
	unknown: "❓",
};

function formatKickoff(value) {
	if (!value) {
		return "-";
	}

	const parsedDate = new Date(value);

	if (Number.isNaN(parsedDate.getTime())) {
		return value;
	}

	return parsedDate.toLocaleString("es-ES", {
		year: "numeric",
		month: "2-digit",
		day: "2-digit",
		hour: "2-digit",
		minute: "2-digit",
		hour12: false,
	});
}

function normalizeMatch(match) {
	const weather = match.weather || {};
	const condition = String(weather.condition || "Cloudy");

	return {
		home_team: match.home_team,
		away_team: match.away_team,
		stadium: match.stadium,
		kickoff: formatKickoff(match.kickoff_datetime || match.kickoff),
		weather_icon: condition.toLowerCase(),
		temperature_c: weather.temperature_c ?? "-",
		humidity_percent: weather.humidity ?? "-",
		wind_speed_kmh: weather.wind_kph ?? "-",
		precipitation_probability_percent: weather.precipitation_probability ?? "-",
	};
}

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

	grid.innerHTML = matches.slice(0, 20).map(createMatchCard).join("");
}

function setLoadingState(isLoading) {
	const loadingState = document.getElementById("loading-state");

	if (!loadingState) {
		return;
	}

	loadingState.classList.toggle("hidden", !isLoading);
}

async function loadMatches() {
	setLoadingState(true);

	try {
		const response = await fetch(API_ENDPOINT);

		if (!response.ok) {
			throw new Error("Failed to load fixtures");
		}

		const matches = await response.json();
		const normalizedMatches = Array.isArray(matches)
			? matches.map(normalizeMatch)
			: fallbackMatches;

		renderMatches(normalizedMatches);
	} catch (error) {
		renderMatches(fallbackMatches);
	} finally {
		setLoadingState(false);
	}
}

document.addEventListener("DOMContentLoaded", loadMatches);
