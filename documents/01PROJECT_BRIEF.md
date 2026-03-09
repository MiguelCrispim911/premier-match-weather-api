# PROJECT_BRIEF

## 1. Resumen del proyecto
Premier Match Weather API es un proyecto pequeño desarrollado con Python y Flask que permitirá consultar el clima esperado para partidos de la Premier League en el estadio donde se jugarán.  
La solución incluirá una API REST como núcleo del sistema y un frontend sencillo para consumirla de forma visual.  
La primera versión buscará cubrir un flujo funcional y presentable, con una estructura ordenada, fácil de explicar y adecuada para un internship.  
El proyecto seguirá un enfoque similar al ejemplo del laboratorio del curso, pero con un alcance un poco más completo.

## 2. Problema a resolver
Actualmente, una persona que quiera conocer el clima esperado para un partido de fútbol debe buscar por separado el estadio, la ciudad, la fecha del partido y luego consultar un servicio meteorológico.

Ese proceso es poco práctico y no ofrece una experiencia integrada.

Vale la pena resolverlo porque permite centralizar información útil en una sola solución, combinando datos de estadios, partidos y clima en una API fácil de consumir, además de una interfaz simple para demostración y uso básico.

## 3. Usuario objetivo
Usuario principal:
- Profesor del internship como evaluador del proyecto.

Usuario final imaginario:
- Aficionados al fútbol.
- Analistas deportivos.
- Personas interesadas en conocer el clima esperado de un partido.

Necesidad del usuario:
- Consultar de forma rápida y clara el pronóstico del tiempo esperado para un estadio o partido de la Premier League.
- Ver esta información tanto en formato JSON como en una interfaz visual sencilla.

## 4. Objetivo del proyecto

Objetivo principal:
- Construir una solución pequeña y funcional basada en Flask que permita consultar el clima esperado para estadios o partidos de la Premier League, con una API REST y un frontend simple.

Objetivos secundarios:
- Demostrar una estructura de proyecto limpia y defendible.
- Integrar al menos una API externa de forma clara.
- Incluir manejo básico de errores, logging y pruebas.
- Contar con una interfaz visual sencilla y agradable para facilitar la demostración.
- Utilizar IA como apoyo para diseño e implementación.

## 5. Alcance de la versión 1 (v1)

La primera versión incluirá:

- Endpoint de salud de la API.
- Endpoint para listar los estadios de la Premier League.
- Endpoint para consultar el clima en un estadio específico para una fecha y hora.
- Endpoint opcional para consultar el clima de un partido usando datos de fixtures de una API externa.
- Respuestas en formato JSON.
- Manejo básico de errores.
- Logging básico de requests.
- Pruebas automáticas con pytest.
- Estructura de proyecto organizada.
- README con instrucciones de instalación y uso.
- Frontend sencillo para consultar información de la API desde el navegador.
- Interfaz visual simple pero agradable, enfocada en demostración más que en complejidad.

## 6. Fuera de alcance

No se incluirá en esta versión:

- Modelo propio de predicción meteorológica.
- Procesamiento avanzado de datos climáticos.
- Autenticación o control de usuarios.
- Frontend complejo con múltiples vistas avanzadas.
- Despliegue obligatorio en la nube.
- Funcionalidades tipo sistema enterprise.
- Persistencia compleja de datos.
- Panel administrativo.

## 7. Requisitos funcionales

1. La API debe exponer un endpoint `GET /health` que confirme que el servicio está funcionando.
2. La API debe permitir consultar la lista de estadios de la Premier League.
3. La API debe permitir consultar información de un estadio específico.
4. La API debe permitir consultar el pronóstico del clima para un estadio dado una fecha y hora.
5. La API debe retornar respuestas en formato JSON.
6. La API debe devolver errores estructurados cuando una solicitud sea inválida.
7. La API debe integrar una API externa de clima para obtener pronósticos.
8. Si es viable, la API debe permitir consultar el clima de un partido usando datos de fixtures de una API externa.
9. El sistema debe incluir una página web sencilla que consuma la API.
10. El frontend debe permitir al menos seleccionar o ingresar un estadio y una fecha/hora para consultar el clima.
11. El frontend debe mostrar el resultado de forma clara para la demostración.
12. La solución debe incluir pruebas automáticas básicas para los endpoints principales.

## 8. Requisitos no funcionales

1. El proyecto debe estar escrito en Python usando Flask.
2. La API debe poder ejecutarse localmente sin dependencias complejas.
3. El proyecto debe tener una estructura clara de carpetas y archivos.
4. El código debe ser legible y fácil de explicar durante la evaluación.
5. El proyecto debe incluir logging básico de requests.
6. El proyecto debe incluir pruebas automatizadas con pytest.
7. El frontend debe ser simple, rápido de implementar y fácil de mantener.
8. La interfaz debe verse ordenada y agradable, aunque sea mínima.
9. El proyecto completo debe poder enviarse por correo como archivo comprimido.

## 9. Restricciones y decisiones obligatorias

Tecnologías obligatorias:
- Python
- Flask
- pytest para pruebas

Restricciones del proyecto:
- Debe ser un proyecto pequeño y realista para un internship.
- Debe priorizar simplicidad, claridad y funcionalidad.
- Debe demostrar uso de IA en el proceso de desarrollo.

Restricciones académicas y de entrega:
- Debe poder ejecutarse localmente.
- Debe incluir README con instrucciones claras.
- Debe poder enviarse por correo como archivo comprimido.
- La primera versión no debe depender de una arquitectura compleja.

## 10. Recomendaciones técnicas iniciales

Uso de APIs externas para clima:
- Sí, v1 debería consumir una API meteorológica externa.
- Es la opción más realista para un proyecto pequeño, ya que evita construir lógica de predicción fuera del alcance.
- Permite concentrar el esfuerzo en integración, estructura, validación y experiencia de uso.

Uso de APIs externas para fixtures:
- Sí, v1 puede consumir una API externa de fixtures si el tiempo lo permite.
- Esta integración debe considerarse una mejora viable, no una dependencia absoluta del MVP.
- Si complica demasiado el alcance, v1 puede centrarse primero en clima por estadio y fecha/hora.

Uso de base de datos:
- No, v1 debería evitar base de datos.
- Los estadios pueden mantenerse en un archivo estático o estructura en memoria.
- Esto reduce complejidad, acelera el desarrollo y hace el proyecto más fácil de explicar y entregar.
- Una base de datos solo tendría sentido en una versión futura con más persistencia, historial o cache.

Recomendación para el frontend:
- El frontend más conveniente para v1 es una interfaz sencilla servida por Flask usando plantillas HTML y CSS simple.
- Esta opción es más fácil y rápida que separar backend y frontend con frameworks modernos.
- Permite lograr una presentación visual agradable sin aumentar demasiado la complejidad técnica.

## 11. Supuestos

- La lista de estadios de la Premier League puede mantenerse como un archivo estático en el proyecto.
- La API meteorológica elegida tendrá un plan gratuito o suficiente para pruebas.
- El frontend será de una sola página o de muy pocas vistas.
- El frontend servirá principalmente para demostración local.
- El proyecto será evaluado sobre todo por claridad, estructura, funcionamiento y capacidad de defensa técnica.
- La fecha de entrega aún no está definida y deberá completarse más adelante.

## 12. Riesgos principales

Riesgos técnicos:
- Dependencia de APIs externas que puedan cambiar, fallar o limitar solicitudes.
- Dificultad para encontrar una API gratuita y simple para fixtures.
- Posibles problemas al mapear estadios con ubicaciones correctas para obtener el clima.

Riesgos de alcance:
- Intentar incluir demasiadas funcionalidades en la primera versión.
- Convertir un frontend simple en una tarea más grande de lo necesario.

Riesgos de tiempo:
- Subestimar el tiempo necesario para integración con APIs externas.
- Invertir demasiado tiempo en diseño visual en lugar de funcionalidad principal.

## 13. Definición de terminado

El proyecto se considera terminado cuando:

- La aplicación corre localmente sin errores.
- El endpoint `/health` funciona correctamente.
- Existe un endpoint para listar estadios.
- Existe un endpoint para consultar clima por estadio y fecha/hora.
- La API devuelve respuestas JSON claras y consistentes.
- Los errores se manejan con respuestas JSON estructuradas.
- El proyecto incluye logging básico.
- El proyecto incluye pruebas automatizadas que corren correctamente con pytest.
- Existe un frontend sencillo funcional accesible desde el navegador.
- El frontend permite hacer al menos una consulta útil al sistema.
- La interfaz muestra resultados de forma clara y presentable.
- Existe un README con instrucciones de instalación y uso.
- El proyecto puede comprimirse y enviarse por correo sin pasos complejos adicionales.

## 14. Próximos pasos sugeridos

1. Ajustar la estructura base del proyecto Flask tomando como referencia el laboratorio del curso.
2. Definir la lista estática de estadios de la Premier League para v1.
3. Implementar el endpoint `/health`.
4. Implementar el endpoint para listar estadios.
5. Investigar y seleccionar una API meteorológica adecuada para el MVP.
6. Implementar la consulta de clima por estadio y fecha/hora.
7. Crear un frontend sencillo con plantilla HTML, estilos básicos y formulario de consulta.
8. Conectar el frontend con la API para mostrar resultados.
9. Agregar manejo básico de errores y logging.
10. Escribir pruebas automáticas con pytest.
11. Documentar instalación, uso de endpoints y uso del frontend en el README.