# SCAFFOLDING

## 1. Propósito del scaffolding

Este documento define el scaffolding inicial de **Premier Match Weather API** para dejar preparada una base ordenada, pequeña y defendible sobre Flask, alineada con el brief del proyecto y con una arquitectura por capas simple.

El objetivo de esta fase no es implementar toda la lógica del sistema, sino dejar listo lo siguiente:

- estructura de carpetas coherente
- app factory funcional
- blueprints separados por responsabilidad
- configuración base
- manejo inicial de errores y logging
- repositorio estático de estadios
- frontend mínimo servido por Flask
- tests base preparados para crecer por fases

Al terminar esta etapa, el proyecto debe poder arrancar localmente, exponer endpoints base y dejar puntos claros de extensión para implementar después la lógica real de clima y posibles fixtures.

---

## 2. Árbol inicial del proyecto

```text
premier-match-weather-api/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ config.py
│  ├─ logging_config.py
│  ├─ data/
│  │  └─ stadiums.json
│  ├─ routes/
│  │  ├─ __init__.py
│  │  ├─ fixtures.py
│  │  ├─ health.py
│  │  ├─ stadiums.py
│  │  ├─ weather.py
│  │  └─ frontend.py
│  ├─ services/
│  │  ├─ __init__.py
│  │  ├─ fixture_service.py
│  │  ├─ stadium_service.py
│  │  └─ weather_service.py
│  ├─ clients/
│  │  ├─ __init__.py
│  │  └─ weather_api_client.py
│  ├─ repositories/
│  │  ├─ __init__.py
│  │  ├─ stadium_repository.py
│  │  └─ fixture_repository.py
│  ├─ errors/
│  │  ├─ __init__.py
│  │  ├─ exceptions.py
│  │  └─ handlers.py
│  ├─ utils/
│  │  ├─ __init__.py
│  │  ├─ datetime_utils.py
│  │  └─ validation.py
│  ├─ templates/
│  │  └─ index.html
│  └─ static/
│     ├─ css/
│     │  └─ styles.css
│     └─ js/
│        └─ app.js
├─ tests/
│  ├─ __init__.py
│  ├─ conftest.py
│  ├─ test_health.py
│  ├─ test_stadiums.py
│  ├─ test_weather.py
│  └─ test_frontend.py
├─ .env.example
├─ .gitignore
├─ requirements.txt
└─ README.md
```

---

## 3. Descripción de cada archivo y carpeta

### Carpeta `app/`
Contiene toda la aplicación Flask. Existe para concentrar la lógica principal en un paquete importable y compatible con app factory.

### `app/__init__.py`
Punto de creación de la aplicación mediante `create_app()`. Existe para centralizar configuración, registro de blueprints, logging y handlers de errores. Debe tener implementación mínima funcional en esta fase.

### `app/main.py`
Punto de arranque local. Existe para ejecutar la app fácilmente durante desarrollo. Debe tener código real mínimo.

### `app/config.py`
Configuración básica por variables de entorno. Existe para evitar valores hardcodeados repartidos por el proyecto. Debe tener implementación mínima funcional.

### `app/logging_config.py`
Configuración de logging básico de requests. Existe porque el brief exige logging simple y defendible. Debe tener implementación funcional básica.

### Carpeta `app/data/`
Almacena datos estáticos del proyecto. Existe porque v1 evita base de datos. En esta fase sí debe incluir `stadiums.json`.

### `app/data/stadiums.json`
Fuente estática inicial de estadios. Existe para soportar el endpoint de listado y futuras búsquedas por estadio. Debe contener datos reales mínimos.

### `app/data/fixtures.json`
Archivo de datos estático que contiene la lista de fixtures (partidos) restantes de la temporada de la Premier League. Existe para permitir que la API devuelva información de partidos sin depender de una API externa de fútbol. Cada fixture incluye el equipo local, el equipo visitante, el stadium_id correspondiente y la fecha y hora de inicio del partido. Este archivo sirve como fuente de datos para el fixture_repository.

### Carpeta `app/routes/`
Contiene blueprints HTTP. Existe para separar endpoints por responsabilidad y mantener la app pequeña pero ordenada.

### `app/routes/health.py`
Endpoint de salud. Debe ser implementación mínima funcional real.

### `app/routes/stadiums.py`
Endpoints relacionados con estadios. Debe ser funcional al menos para listar estadios y, si se desea, dejar preparado un detalle por id o slug.

### `app/routes/weather.py`
Endpoints relacionados con clima. En esta fase puede quedar como placeholder o stub mínimo, sin integración completa con API externa.

### `app/routes/frontend.py`
Ruta para servir la página principal HTML. Debe tener implementación funcional mínima.

### `app/routes/frontend.py`
Define los endpoints HTTP relacionados con fixtures (partidos). Su responsabilidad es recibir las solicitudes HTTP, delegar la lógica al fixture_service y devolver respuestas JSON al cliente. En esta fase debe exponer al menos un endpoint que permita obtener la lista de fixtures disponibles.


### Carpeta `app/services/`
Orquesta lógica de aplicación. Existe para evitar que la lógica de negocio quede dentro de las rutas.

### `app/services/stadium_service.py`
Capa intermedia entre rutas y repositorio de estadios. Debe contener funciones simples reales.

### `app/services/weather_service.py`
Encapsula la lógica futura para clima. En esta fase debe quedar como stub o implementación mínima con firmas y docstrings.

### `app/services/fixture_service.py`
Contiene la lógica de aplicación relacionada con fixtures. Actúa como capa intermedia entre las rutas y el repositorio de fixtures. Se encarga de obtener los partidos desde fixture_repository, ordenar o filtrar los resultados cuando sea necesario y devolver los próximos partidos que serán utilizados por la API y el frontend.


### Carpeta `app/clients/`
Encapsula clientes HTTP externos. Existe porque el consumo de API meteorológica debe estar aislado de rutas y servicios.

### `app/clients/weather_api_client.py`
Base del cliente de clima. En esta fase no debe incluir integración completa, pero sí estructura, firmas y manejo inicial de configuración.

### Carpeta `app/repositories/`
Acceso a fuentes de datos internas. Existe para abstraer la lectura del archivo JSON de estadios.

### `app/repositories/fixture_repository.py`

Encapsula el acceso a los datos de fixtures almacenados en fixtures.json. Su responsabilidad es leer el archivo, convertir los datos a estructuras Python y proporcionar funciones simples que permitan al fixture_service acceder a la lista de partidos sin depender directamente del formato del archivo

### `app/repositories/stadium_repository.py`
Lectura de `stadiums.json`. Debe tener implementación funcional mínima.

### Carpeta `app/errors/`
Manejo centralizado de excepciones y respuestas JSON de error. Existe porque el brief exige errores estructurados.

### `app/errors/exceptions.py`
Define excepciones custom simples como `AppError`, `NotFoundError`, `ValidationError`, `ExternalServiceError`. En esta fase sí debe existir.

### `app/errors/handlers.py`
Registro de error handlers globales. Debe tener implementación mínima funcional.

### Carpeta `app/utils/`
Utilidades pequeñas compartidas. Existe para mantener limpio el resto del código.

### `app/utils/datetime_utils.py`
Funciones auxiliares para parseo o validación básica de fecha/hora. En scaffolding debe quedar como helper mínimo o placeholder documentado.

### `app/utils/validation.py`
Validaciones simples de parámetros. Puede quedar con helpers mínimos y lugar claro para crecer.

### Carpeta `app/templates/`
Plantillas HTML servidas por Flask. Existe porque el frontend será sencillo y server-rendered.

### `app/templates/index.html`
Pantalla principal del frontend. Debe ser funcional mínimamente.

### Carpeta `app/static/`
Archivos estáticos del frontend.

### `app/static/css/styles.css`
Estilos básicos para que la interfaz se vea ordenada y agradable. Debe tener implementación mínima real.

### `app/static/js/app.js`
Lógica del frontend para consumir la API y renderizar resultados. Debe quedar con implementación mínima o placeholder claro según la fase.

### Carpeta `tests/`
Pruebas automáticas con pytest. Existe porque el brief exige tests base.

### `tests/conftest.py`
Fixtures compartidas como `app` y `client`. Debe tener implementación funcional mínima.

### `tests/test_health.py`
Prueba del endpoint `/health`. Debe estar funcional desde esta fase.

### `tests/test_stadiums.py`
Pruebas del endpoint de estadios. Debe cubrir al menos el listado.

### `tests/test_weather.py`
Pruebas base del endpoint de clima. En esta fase puede validar placeholder o comportamiento no implementado todavía, según decisión de implementación mínima.

### `tests/test_frontend.py`
Prueba básica de carga del frontend. Debe verificar que `/` responda correctamente.

### `.env.example`
Variables de entorno documentadas. Existe para que el proyecto sea fácil de configurar y enviar.

### `.gitignore`
Ignora entorno virtual, cachés y archivos locales. Debe existir desde el inicio.

### `requirements.txt`
Dependencias del proyecto. Debe contener solo lo necesario para empezar.

### `README.md`
Documentación de instalación y uso. En scaffolding puede quedar inicial, breve y ampliable.

---

## 4. Archivos a crear en la fase de scaffolding

### Núcleo de aplicación
- `app/__init__.py`
- `app/main.py`
- `app/config.py`
- `app/logging_config.py`

### Rutas
- `app/routes/__init__.py`
- `app/routes/health.py`
- `app/routes/stadiums.py`
- `app/routes/weather.py`
- `app/routes/frontend.py`

### Servicios
- `app/services/__init__.py`
- `app/services/stadium_service.py`
- `app/services/weather_service.py`

### Clientes externos
- `app/clients/__init__.py`
- `app/clients/weather_api_client.py`

### Repositorios
- `app/repositories/__init__.py`
- `app/repositories/stadium_repository.py`

### Errores
- `app/errors/__init__.py`
- `app/errors/exceptions.py`
- `app/errors/handlers.py`

### Utilidades
- `app/utils/__init__.py`
- `app/utils/datetime_utils.py`
- `app/utils/validation.py`

### Datos
- `app/data/stadiums.json`

### Frontend
- `app/templates/index.html`
- `app/static/css/styles.css`
- `app/static/js/app.js`

### Tests
- `tests/__init__.py`
- `tests/conftest.py`
- `tests/test_health.py`
- `tests/test_stadiums.py`
- `tests/test_weather.py`
- `tests/test_frontend.py`

### Archivos raíz
- `requirements.txt`
- `.env.example`
- `.gitignore`
- `README.md`

---

## 5. Contenido mínimo esperado por archivo

### `app/__init__.py`
**Debe contener en esta fase:**
- función `create_app()`
- carga de configuración
- registro de blueprints
- registro de handlers de errores
- inicialización de logging

**No debe contener todavía:**
- lógica de negocio
- llamadas a APIs externas
- validaciones complejas

**Tipo:** implementación mínima funcional.

---

### `app/main.py`
**Debe contener en esta fase:**
- import de `create_app`
- creación de `app`
- arranque local con host/port configurables

**No debe contener todavía:**
- lógica adicional de aplicación

**Tipo:** implementación mínima funcional.

---

### `app/config.py`
**Debe contener en esta fase:**
- clase `Config`
- lectura de variables de entorno
- flags como `DEBUG`, `TESTING`
- variable para API key y base URL de clima

**No debe contener todavía:**
- configuraciones por entorno demasiado complejas
- clases innecesarias para producción

**Tipo:** implementación mínima funcional.

---

### `app/routes/__init__.py`
**Debe contener en esta fase:**
- imports o helper para centralizar blueprints, si se quiere
- organización simple del paquete

**No debe contener todavía:**
- lógica de endpoints

**Tipo:** placeholder ligero.

---

### `app/routes/health.py`
**Debe contener en esta fase:**
- blueprint, por ejemplo `health_bp`
- endpoint `GET /health`
- respuesta JSON simple como `{"status": "ok"}`

**No debe contener todavía:**
- chequeos complejos de dependencias externas

**Tipo:** implementación mínima funcional.

---

### `app/routes/stadiums.py`
**Debe contener en esta fase:**
- blueprint `stadiums_bp`
- endpoint `GET /stadiums`
- opcionalmente `GET /stadiums/<stadium_id>` o `/<slug>`
- uso de `stadium_service`

**No debe contener todavía:**
- filtros avanzados
- persistencia en base de datos
- lógica compleja de búsqueda

**Tipo:** implementación mínima funcional para listado; detalle opcional y simple.

---

### `app/routes/weather.py`
**Debe contener en esta fase:**
- blueprint `weather_bp`
- endpoint planeado para consulta de clima, por ejemplo `GET /weather`
- firma esperada de parámetros: estadio y fecha/hora
- respuesta placeholder clara o stub controlado si aún no hay integración

**No debe contener todavía:**
- integración completa con API meteorológica
- transformación avanzada de datos externos

**Tipo:** stub o implementación mínima funcional muy acotada.

---

### `app/routes/frontend.py`
**Debe contener en esta fase:**
- blueprint `frontend_bp`
- endpoint `GET /`
- render de `index.html`

**No debe contener todavía:**
- múltiples vistas
- lógica compleja del lado servidor

**Tipo:** implementación mínima funcional.

---

### `app/services/stadium_service.py`
**Debe contener en esta fase:**
- funciones como `get_all_stadiums()` y opcionalmente `get_stadium_by_id()` o `get_stadium_by_slug()`
- uso de `stadium_repository`
- docstrings claros

**No debe contener todavía:**
- reglas complejas
- cache
- lógica innecesaria

**Tipo:** implementación mínima funcional.

---

### `app/services/weather_service.py`
**Debe contener en esta fase:**
- firma de función como `get_weather_for_stadium_at_datetime(...)`
- docstrings que expliquen inputs y output esperado
- posible llamada futura al cliente de clima
- manejo inicial de “not implemented yet” si aplica

**No debe contener todavía:**
- integración completa
- reglas de matching avanzadas
- lógica de fixtures

**Tipo:** stub bien definido.

---

### `app/clients/weather_api_client.py`
**Debe contener en esta fase:**
- clase o funciones base para cliente HTTP
- lectura de API key y base URL desde config
- método placeholder para consulta futura de pronóstico

**No debe contener todavía:**
- integración total
- manejo avanzado de rate limits
- retries complejos

**Tipo:** placeholder estructural o stub.

---

### `app/repositories/stadium_repository.py`
**Debe contener en esta fase:**
- lectura del archivo `stadiums.json`
- función como `load_stadiums()`
- opcionalmente búsquedas simples por id, name o slug

**No debe contener todavía:**
- abstracciones excesivas
- patrones complejos

**Tipo:** implementación mínima funcional.

---

### `app/errors/exceptions.py`
**Debe contener en esta fase:**
- excepción base `AppError`
- excepciones específicas simples:
  - `ValidationError`
  - `NotFoundError`
  - `ExternalServiceError`

**No debe contener todavía:**
- jerarquías excesivamente profundas

**Tipo:** implementación simple real.

---

### `app/errors/handlers.py`
**Debe contener en esta fase:**
- función `register_error_handlers(app)`
- handlers para:
  - 404
  - 500
  - `AppError`
- respuesta JSON estructurada con tipo y mensaje

**No debe contener todavía:**
- manejo sofisticado de observabilidad

**Tipo:** implementación mínima funcional.

---

### `app/utils/datetime_utils.py`
**Debe contener en esta fase:**
- helper simple para parsear fecha/hora
- docstring del formato esperado

**No debe contener todavía:**
- manejo complejo de zonas horarias
- librerías pesadas innecesarias

**Tipo:** placeholder útil o helper mínimo.

---

### `app/utils/validation.py`
**Debe contener en esta fase:**
- validaciones pequeñas de parámetros requeridos
- helpers reutilizables por rutas o servicios

**No debe contener todavía:**
- framework propio de validación

**Tipo:** implementación mínima o placeholder ligero.

---

### `app/logging_config.py`
**Debe contener en esta fase:**
- configuración básica de logger
- logging de request y response
- campos mínimos como método, path, status, duración

**No debe contener todavía:**
- logging estructurado avanzado
- integración con servicios externos

**Tipo:** implementación mínima funcional.

---

### `app/templates/index.html`
**Debe contener en esta fase:**
- layout simple
- título del proyecto
- formulario básico para consultar por estadio y fecha/hora
- contenedor para mostrar resultados
- referencias a CSS y JS

**No debe contener todavía:**
- diseño complejo
- múltiples páginas
- framework frontend pesado

**Tipo:** implementación mínima funcional.

---

### `app/static/css/styles.css`
**Debe contener en esta fase:**
- estilos básicos para presentación limpia y agradable
- layout sencillo y responsive básico

**No debe contener todavía:**
- sistema de diseño complejo
- dependencias visuales pesadas

**Tipo:** implementación mínima funcional.

---

### `app/static/js/app.js`
**Debe contener en esta fase:**
- lógica básica para leer formulario
- llamada simple a endpoint correspondiente
- render básico de resultados o errores
- si el endpoint de clima aún no está listo, puede mostrar mensaje controlado

**No debe contener todavía:**
- arquitectura JS compleja
- librerías de frontend innecesarias

**Tipo:** mínima funcional o placeholder claro.

---

### `app/data/stadiums.json`
**Debe contener en esta fase:**
- lista inicial de estadios con campos simples y consistentes
- campos recomendados:
  - `id`
  - `name`
  - `club`
  - `city`
  - `country`
  - `latitude`
  - `longitude`

**No debe contener todavía:**
- información excesiva
- formato inconsistente

**Tipo:** dato real mínimo funcional.

---

### `tests/conftest.py`
**Debe contener en esta fase:**
- fixture `app`
- fixture `client`
- configuración de testing

**No debe contener todavía:**
- mocks complejos si aún no son necesarios

**Tipo:** implementación mínima funcional.

---

### `tests/test_health.py`
**Debe contener en esta fase:**
- prueba de status code
- prueba de JSON esperado en `/health`

**No debe contener todavía:**
- casos innecesarios

**Tipo:** implementación mínima funcional.

---

### `tests/test_stadiums.py`
**Debe contener en esta fase:**
- prueba de listado de estadios
- verificación de estructura JSON básica

**No debe contener todavía:**
- tests complejos de filtros no implementados

**Tipo:** implementación mínima funcional.

---

### `tests/test_weather.py`
**Debe contener en esta fase:**
- prueba base del endpoint de clima según comportamiento inicial
- si el endpoint es placeholder, testear ese contrato temporal de forma explícita

**No debe contener todavía:**
- mocks avanzados de API externa si aún no se implementa integración

**Tipo:** test preparado para evolución.

---

### `tests/test_frontend.py`
**Debe contener en esta fase:**
- prueba de que `/` carga correctamente
- verificación básica de contenido HTML

**No debe contener todavía:**
- tests E2E complejos

**Tipo:** implementación mínima funcional.

---

### `.env.example`
**Debe contener en esta fase:**
- `FLASK_ENV=development`
- `PORT=8000`
- `WEATHER_API_BASE_URL=...`
- `WEATHER_API_KEY=your_api_key_here`

**No debe contener todavía:**
- secretos reales

**Tipo:** archivo de referencia.

---

### `requirements.txt`
**Debe contener en esta fase:**
- dependencias mínimas obligatorias

**No debe contener todavía:**
- librerías no usadas

**Tipo:** funcional y pequeño.

---

### `README.md`
**Debe contener en esta fase:**
- propósito breve
- instalación
- ejecución local
- tests
- endpoints iniciales

**No debe contener todavía:**
- documentación extensa prematura

**Tipo:** inicial y ampliable.

---

## 6. Dependencias iniciales

### Obligatorias para empezar
- `Flask`
- `python-dotenv`
- `pytest`
- `requests`

### Opcionales para fases posteriores
- `pytest-mock`
- `coverage` o `pytest-cov`
- `Flask-CORS` solo si después hiciera falta
- `gunicorn` solo si luego se prepara despliegue
- una librería de parsing de fechas adicional solo si la validación lo exige

---

## 7. Orden recomendado de creación

1. Crear estructura de carpetas y archivos vacíos.
2. Crear `requirements.txt`, `.gitignore` y `.env.example`.
3. Implementar `app/config.py`.
4. Implementar `app/__init__.py` con app factory.
5. Implementar `app/logging_config.py`.
6. Implementar `app/errors/exceptions.py` y `app/errors/handlers.py`.
7. Crear `app/data/stadiums.json`.
8. Implementar `app/repositories/stadium_repository.py`.
9. Implementar `app/services/stadium_service.py`.
10. Implementar blueprints:
    - `health.py`
    - `stadiums.py`
    - `frontend.py`
11. Registrar blueprints en la app factory.
12. Crear `app/templates/index.html`.
13. Crear `app/static/css/styles.css`.
14. Crear `app/static/js/app.js`.
15. Dejar preparado `app/routes/weather.py`, `app/services/weather_service.py` y `app/clients/weather_api_client.py` como stubs coherentes.
16. Implementar `app/main.py`.
17. Crear `tests/conftest.py`.
18. Crear tests base de health, stadiums y frontend.
19. Crear test base de weather alineado con el estado real del endpoint.
20. Completar `README.md` inicial.

---

## 8. Qué debe quedar funcional al terminar el scaffolding

Al finalizar esta fase deberían funcionar estas capacidades:

- la app arranca localmente
- existe `create_app()` con app factory
- los blueprints están registrados correctamente
- `GET /health` responde exitosamente
- `GET /stadiums` devuelve una lista de estadios desde `stadiums.json`
- el frontend básico en `/` carga en el navegador
- existe manejo básico de errores JSON
- existe logging básico de requests
- existe estructura preparada para integrar la API meteorológica
- existen tests base que ya pueden correr o empezar a ajustarse
- el proyecto ya tiene una forma defendible, ordenada y académicamente clara

---

## 9. Qué queda pendiente para la siguiente fase

Todavía no debe quedar implementado por completo en el scaffolding:

- integración real con la API meteorológica externa
- consulta de clima real por estadio y fecha/hora
- lógica de selección del forecast más cercano a la hora solicitada
- integración opcional con API de fixtures
- validaciones completas de entrada
- cobertura amplia de errores de servicios externos
- tests completos con mocks de API externa
- refinamiento visual del frontend
- documentación final completa del proyecto

---

## 10. Próximo prompt recomendado

```text
Actúa como Senior Python/Flask Developer.

Ya existe el archivo `SCAFFOLDING.md` del proyecto Premier Match Weather API.

Quiero que implementes ahora la versión mínima funcional inicial del proyecto siguiendo exactamente ese scaffolding.

Objetivo de esta fase:
- implementar la app factory
- implementar `GET /health`
- implementar `GET /stadiums`
- cargar los datos desde `app/data/stadiums.json`
- registrar blueprints
- dejar el frontend `/` cargando una página HTML simple
- agregar manejo básico de errores JSON
- agregar tests mínimos para `/health`, `/stadiums` y `/`

Instrucciones:
1. Devuélveme el contenido completo de cada archivo necesario.
2. Usa Flask y pytest.
3. No implementes todavía integración real con API meteorológica.
4. Mantén el proyecto pequeño, claro y ejecutable localmente.
5. Si un archivo aún no necesita lógica completa, déjalo como placeholder coherente.
6. Incluye también un `requirements.txt`, `.env.example` y `README.md` mínimos.
```

---

## Nota de implementación

Este scaffolding prioriza una arquitectura simple por capas:

- **routes** para exponer HTTP
- **services** para coordinar casos de uso
- **repositories** para datos internos
- **clients** para integraciones externas
- **errors** para respuestas consistentes
- **templates/static** para un frontend mínimo con Flask

Es una estructura suficientemente limpia para defender técnicamente el proyecto sin sobrediseñarlo.

