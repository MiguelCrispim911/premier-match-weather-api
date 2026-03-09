# DISEÑO TÉCNICO — Premier Match Weather API

## 1. Propósito del documento

Este documento define el diseño técnico base de la **Premier Match Weather API**, un proyecto pequeño de internship construido con **Python + Flask**.

Su objetivo es servir como contexto técnico único antes de programar, para que la implementación se mantenga simple, ordenada, defendible y alineada con un MVP realista.

---

## 2. Resumen técnico del sistema

La aplicación será una **API REST en Flask** con un **frontend sencillo** servido por la misma aplicación.

El sistema permitirá:

- consultar estadios de la Premier League
- consultar el clima esperado en un estadio para una fecha y hora específicas
- mostrar esa consulta desde un frontend simple, funcional y visualmente agradable

### 2.1 Flujo general

1. El usuario hace una consulta desde el frontend o directamente por HTTP.
2. La API recibe parámetros como `stadium_id` y `datetime`.
3. La aplicación valida la entrada.
4. La aplicación busca el estadio en un catálogo local.
5. Con las coordenadas del estadio, consulta una API meteorológica externa.
6. La respuesta externa se transforma a un formato JSON propio y consistente.
7. El frontend muestra el resultado de manera clara.

### 2.2 Estrategia de resolución del estadio

En v1, los estadios se resolverán desde un archivo local, por ejemplo `stadiums.json`.

Cada estadio debe tener como mínimo:

- `id`
- `name`
- `team`
- `city`
- `latitude`
- `longitude`
- `timezone`

Esto evita usar base de datos en la primera versión y reduce complejidad innecesaria.

### 2.3 Estrategia de resolución del clima

La API tomará:

- latitud del estadio
- longitud del estadio
- fecha y hora solicitadas
- zona horaria del estadio

Luego consultará un proveedor externo de clima para obtener el forecast más cercano a la fecha/hora pedida.

### 2.4 Integraciones externas

#### API meteorológica
Integración principal del MVP.

Responsabilidades:

- consultar pronóstico por coordenadas
- devolver datos útiles para una fecha y hora concretas
- permitir mapear la respuesta a un formato propio

#### API de fixtures
Integración opcional de extensión.

Responsabilidades:

- obtener fecha/hora y estadio de un partido
- habilitar endpoints futuros como clima por partido real

No debe ser dependencia obligatoria del core de v1.

---

## 3. Alcance técnico de v1

### 3.1 Endpoints core

#### `GET /health`
Verifica que la API está operativa.

#### `GET /api/stadiums`
Retorna la lista de estadios disponibles.

#### `GET /api/stadiums/<stadium_id>`
Retorna el detalle de un estadio específico.

#### `GET /api/weather/stadium`
Consulta el clima esperado para un estadio en una fecha y hora.

Parámetros recomendados:

- `stadium_id`
- `datetime` en formato ISO 8601

Ejemplo:

`/api/weather/stadium?stadium_id=emirates&datetime=2026-03-15T16:30:00`

#### `GET /`
Sirve el frontend sencillo.

### 3.2 Endpoints opcionales de extensión

#### `GET /api/fixtures`
Permite listar o consultar fixtures si se integra un proveedor externo.

#### `GET /api/fixtures/<match_id>/weather`
Obtiene el clima esperado para un partido usando el fixture y la integración meteorológica.

### 3.3 Priorización

**Obligatorios para v1:**

- `/health`
- `/api/stadiums`
- `/api/stadiums/<stadium_id>`
- `/api/weather/stadium`
- `/`

**Deseables pero opcionales:**

- `/api/fixtures`
- `/api/fixtures/<match_id>/weather`

---

## 4. Requisitos funcionales refinados

1. La API debe exponer un endpoint de salud.
2. La API debe listar los estadios disponibles.
3. La API debe retornar el detalle de un estadio por identificador.
4. La API debe consultar el clima esperado para un estadio y una fecha/hora dadas.
5. La API debe validar la existencia del estadio consultado.
6. La API debe validar formato y presencia de parámetros requeridos.
7. La API debe responder en JSON en todos los endpoints de backend.
8. La API debe integrar un proveedor externo de clima.
9. La API debe mapear la respuesta externa a un formato propio, limpio y simple.
10. La API debe manejar errores con respuestas JSON consistentes.
11. El frontend debe permitir seleccionar un estadio.
12. El frontend debe permitir ingresar fecha y hora.
13. El frontend debe consumir el endpoint de clima y mostrar los resultados.
14. La API debe funcionar localmente sin dependencias innecesarias.
15. La integración con fixtures debe quedar preparada, pero no bloquear el MVP.

---

## 5. Requisitos no funcionales

1. La solución debe tener una estructura clara y fácil de explicar.
2. Debe haber separación entre rutas, servicios, acceso a datos y clientes externos.
3. El manejo de errores debe ser uniforme.
4. Debe existir logging básico.
5. La ejecución local debe ser simple.
6. La aplicación debe ser fácil de testear con `pytest`.
7. La complejidad debe mantenerse baja.
8. La configuración sensible debe manejarse con variables de entorno.
9. El frontend debe ser sencillo pero visualmente agradable.
10. El proyecto debe ser defendible como trabajo de internship.

---

## 6. Casos borde importantes

### 6.1 Estadio inexistente
Si el `stadium_id` no existe en el catálogo local, la API debe responder `404` con un mensaje claro.

### 6.2 Fecha fuera del rango del forecast
Si el proveedor meteorológico no tiene pronóstico para la fecha solicitada, la API debe responder con error controlado, idealmente `400` o `422`.

### 6.3 Parámetros inválidos
Si faltan parámetros o el formato de `datetime` es incorrecto, la API debe responder `400`.

### 6.4 API meteorológica no disponible
Si el proveedor externo falla, responde lento o no devuelve datos útiles, la API debe responder `502` o `503`.

### 6.5 API de fixtures no disponible
Si se implementan endpoints de fixtures y el proveedor falla, ese error no debe romper los endpoints core.

### 6.6 Problemas de zona horaria
La hora del partido debe interpretarse correctamente según la zona horaria del estadio. Este punto es crítico para no consultar un forecast incorrecto.

### 6.7 Datos incompletos del proveedor
Si el proveedor devuelve una respuesta parcial o inesperada, la API debe manejarlo sin exponer errores internos al usuario.

---

## 7. Módulos principales y responsabilidades

### 7.1 `routes`
Responsables de exponer endpoints HTTP.

Deben:

- recibir requests
- validar inputs básicos
- delegar lógica a servicios
- devolver JSON o HTML

### 7.2 `services`
Contienen la lógica de negocio principal.

Deben:

- resolver estadios
- coordinar llamadas a clientes externos
- aplicar reglas del caso de uso
- construir respuestas consistentes

### 7.3 `clients`
Encapsulan llamadas a APIs externas.

Deben:

- construir requests HTTP
- manejar timeouts
- interpretar respuestas externas
- lanzar errores controlados

### 7.4 `repositories`
Gestionan acceso a datos locales.

En v1, su responsabilidad principal será leer el catálogo de estadios desde un archivo JSON.

### 7.5 `models` o `schemas`
Definen la forma esperada de datos internos o respuestas.

No se necesita una capa compleja; puede resolverse con estructuras simples o helpers.

### 7.6 `errors`
Centralizan excepciones personalizadas y handlers globales.

Deben:

- mapear excepciones a códigos HTTP
- devolver errores JSON homogéneos

### 7.7 `config`
Centraliza configuración por entorno.

Debe incluir:

- claves de APIs externas
- URLs base
- timeout
- flags de entorno

### 7.8 `utils`
Contienen funciones auxiliares reutilizables.

Ejemplos:

- parseo de fechas
- normalización de timezone
- validaciones pequeñas

### 7.9 `templates` y `static`
Contienen el frontend simple.

Incluyen:

- HTML principal
- CSS
- JavaScript para consumo de la API

---

## 8. Estructura recomendada del proyecto

```text
premier-match-weather-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── health.py
│   │   ├── stadiums.py
│   │   ├── weather.py
│   │   ├── fixtures.py
│   │   └── frontend.py
│   │
│   ├── services/
│   │   ├── stadium_service.py
│   │   ├── weather_service.py
│   │   └── fixture_service.py
│   │
│   ├── clients/
│   │   ├── weather_api_client.py
│   │   └── fixtures_api_client.py
│   │
│   ├── repositories/
│   │   └── stadium_repository.py
│   │
│   ├── data/
│   │   └── stadiums.json
│   │
│   ├── models/
│   │   └── response_models.py
│   │
│   ├── utils/
│   │   ├── datetime_utils.py
│   │   └── validation.py
│   │
│   ├── errors/
│   │   ├── handlers.py
│   │   └── exceptions.py
│   │
│   ├── logging_config.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       ├── css/
│       │   └── styles.css
│       └── js/
│           └── app.js
│
├── tests/
│   ├── conftest.py
│   ├── test_health.py
│   ├── test_stadiums.py
│   ├── test_weather.py
│   └── test_frontend.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

### Justificación de esta estructura

Esta estructura mantiene el proyecto pequeño, ordenado y fácil de defender. Evita sobreingeniería, pero separa suficientemente bien responsabilidades para que el código no se vuelva desordenado.

---

## 9. Diseño de respuestas de la API

### 9.1 Respuesta exitosa de clima

```json
{
  "stadium": {
    "id": "emirates",
    "name": "Emirates Stadium",
    "team": "Arsenal",
    "city": "London"
  },
  "requested_datetime": "2026-03-15T16:30:00",
  "timezone": "Europe/London",
  "weather": {
    "temperature_c": 12.4,
    "condition": "Cloudy",
    "wind_kph": 18.0,
    "humidity": 71,
    "precipitation_probability": 25
  },
  "source": "weather_api"
}
```

### 9.2 Respuesta de error

```json
{
  "error": {
    "type": "bad_request",
    "message": "Invalid datetime format. Use ISO 8601."
  }
}
```

### 9.3 Criterios de consistencia

Todas las respuestas deben:

- usar JSON en endpoints de API
- mantener nombres de campos estables
- evitar exponer la respuesta cruda del proveedor externo
- devolver errores claros y breves

---

## 10. Plan de implementación por fases

### Fase 1 — Setup base del proyecto

- crear estructura de carpetas
- configurar Flask con app factory
- agregar requirements y variables de entorno

### Fase 2 — Endpoint de salud

- implementar `GET /health`
- agregar test básico

### Fase 3 — Catálogo de estadios

- crear `stadiums.json`
- implementar listado de estadios
- implementar detalle por estadio
- agregar tests

### Fase 4 — Integración meteorológica

- seleccionar proveedor
- crear cliente HTTP
- agregar manejo de timeout y errores

### Fase 5 — Servicio de clima

- validar `stadium_id` y `datetime`
- resolver estadio
- consultar clima externo
- devolver respuesta normalizada

### Fase 6 — Endpoint de clima

- implementar `GET /api/weather/stadium`
- cubrir errores comunes
- agregar tests con mocks

### Fase 7 — Frontend sencillo

- construir una página principal
- agregar formulario de consulta
- consumir API con JavaScript
- mostrar resultado con diseño limpio

### Fase 8 — Manejo de errores y logging

- handlers globales
- excepciones custom
- logging básico por request y por error

### Fase 9 — Tests finales

- cubrir endpoints principales
- probar escenarios de error
- mockear dependencias externas

### Fase 10 — README

- documentar instalación
- uso local
- endpoints
- tests
- variables de entorno

### Fase 11 — Extensión opcional de fixtures

- integrar proveedor de partidos
- implementar endpoints opcionales
- resolver clima por partido

---

## 11. Riesgos técnicos

### 11.1 Límites del proveedor meteorológico
El plan gratuito del proveedor podría limitar cantidad de requests o alcance del forecast.

### 11.2 Complejidad de zonas horarias
Un error de timezone puede hacer que el clima consultado no corresponda a la hora real del partido.

### 11.3 Dependencias externas inestables
Los proveedores externos pueden fallar, cambiar su respuesta o imponer restricciones.

### 11.4 Sobreingeniería
Agregar base de datos, autenticación compleja o frontend moderno desde el inicio aumentaría complejidad sin aportar valor al MVP.

### 11.5 Inconsistencia en datos de fixtures
Si se usa un proveedor de fixtures, puede haber diferencias entre nombres de estadio, horarios y formatos.

### 11.6 Tests acoplados a servicios reales
Las pruebas no deben depender de APIs reales. Deben usar mocks.

---

## 12. Decisiones técnicas recomendadas

1. Usar **Flask** por simplicidad y rapidez de implementación.
2. Usar **Blueprints** para separar módulos.
3. Mantener el catálogo de estadios en un archivo JSON local en v1.
4. Usar una sola integración meteorológica principal.
5. Tratar fixtures como mejora opcional.
6. Servir el frontend desde Flask para evitar agregar otro stack.
7. Usar `pytest` para pruebas.
8. Mantener la arquitectura en capas simples: rutas, servicios, clientes y repositorios.
9. Evitar base de datos en la primera versión.
10. Priorizar claridad del proyecto sobre sofisticación técnica.

---

## 13. Conclusión

La **Premier Match Weather API** debe implementarse como un MVP pequeño, limpio y bien estructurado.

La estrategia correcta para esta versión es:

- catálogo local de estadios
- integración meteorológica externa como núcleo funcional
- frontend simple servido por Flask
- separación básica de responsabilidades
- manejo claro de errores
- preparación para una futura extensión con fixtures

Este enfoque permite construir un proyecto realista, funcional y defendible para un contexto de internship sin introducir complejidad innecesaria.