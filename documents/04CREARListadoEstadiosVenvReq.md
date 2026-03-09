# Project Setup

Configuración inicial del entorno de desarrollo para el proyecto
utilizando Python, un entorno virtual y las dependencias necesarias.

------------------------------------------------------------------------

## 1. Crear entorno virtual

Se crea un entorno virtual para aislar las dependencias del proyecto.

``` cmd
py -3.13 -m venv .venv
```

------------------------------------------------------------------------

## 2. Activar entorno virtual

Antes de instalar dependencias o ejecutar el proyecto, se debe activar
el entorno virtual.

``` cmd
.\.venv\Scripts\Activate.ps1
```

------------------------------------------------------------------------

## 3. Instalar dependencias

Instalar las librerías necesarias para el proyecto.

``` cmd
pip install Flask pytest python-dotenv requests
```

Breve descripción de cada dependencia:

-   **Flask** → Framework para construir la API REST.
-   **pytest** → Framework para ejecutar pruebas automatizadas.
-   **python-dotenv** → Permite cargar variables de entorno desde
    archivos `.env`.
-   **requests** → Librería para realizar llamadas HTTP a APIs externas.

------------------------------------------------------------------------

## 4. Generar archivo `requirements.txt`

Guardar todas las dependencias instaladas en un archivo para poder
reproducir el entorno.

``` cmd
pip freeze > requirements.txt
```

Esto permite instalar las mismas dependencias posteriormente usando:

``` cmd
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 5. Configurar `.gitignore`

El archivo `.gitignore` evita que archivos innecesarios o sensibles se
suban al repositorio.

Contenido recomendado:

``` gitignore
# Virtual environments
.venv/
venv/
env/

# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# Environment variables
.env

# VS Code
.vscode/

# OS files
.DS_Store
Thumbs.db

# Python build
build/
dist/
*.egg-info/

# Test cache
.pytest_cache/

# Logs
*.log
```

------------------------------------------------------------------------

## Resultado

Después de completar estos pasos el proyecto queda preparado con:

-   Entorno virtual configurado\
-   Dependencias instaladas\
-   Archivo `requirements.txt` generado\
-   Archivo `.gitignore` configurado

Con esta base el proyecto está listo para comenzar el desarrollo de la
API Flask.
