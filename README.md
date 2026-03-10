# Premier Match Weather API

API en Flask para consultar los próximos partidos de Premier League y su pronóstico meteorológico.

La aplicación:
- Expone fixtures (próximos partidos) desde datos locales reales de la temporada (archivo local).
- Enriquece fixtures con clima usando Open-Meteo.
- Incluye frontend simple para visualizar partidos y clima.

## Calidad y testing

La suite de `pytest` cubre:
- health y estructura de respuesta JSON
- estadios y conteo
- fixtures (lista, orden, por número, por equipo, por fecha, errores JSON)
- weather fixtures (lista, por número, por equipo, por fecha, errores JSON)

Ejecutar tests:



## Cómo iniciar

```powershell
python -m app.main
```

Servidor local:
- `http://127.0.0.1:5000`

## Ejemplos de uso de endpoints (PowerShell)

### Health

```powershell
Invoke-RestMethod "http://127.0.0.1:5000/health"
```

### Fixtures (lista y por número)

```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures"
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/1"
```

### Weather de fixtures (lista y por número)

```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/weather"
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/weather/3"
```

### Fixture weather por estadio y kickoff

```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/weather/stadium/Emirates%20Stadium/kickoff/2026-04-11T12:30:00"
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/weather/stadium/Stamford%20Bridge/kickoff/2026-04-12T16:30:00"
```

### Fixtures por equipo

```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/team/Arsenal"
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/team/Manchester%20United"
```

### Weather por equipo

```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/weather/team/Chelsea"
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/weather/team/Tottenham%20Hotspur"
```

### Fixtures por fecha

```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/date/2026-04-11"
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/date/2026-04-18"
```

### Weather por fecha

```powershell
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/weather/date/2026-04-11"
Invoke-RestMethod "http://127.0.0.1:5000/api/fixtures/weather/date/2026-04-18"
```
```powershell
pytest -q
```