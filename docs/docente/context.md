# Contexto de Vibe Check

## Para quién es

Este repositorio acompaña un curso para personas sin experiencia en programación. El alumno ve primero un panel de referencia, entiende su utilidad, escribe en papel su solución y la reconstruye con IA en otra carpeta.

El caso de uso es una persona que crea contenido y necesita explorar el tono de muchos comentarios. Un panel permite contar, filtrar y revisar ejemplos. Analizar el tono del texto no determina cómo se siente su autor.

## Qué debe aprender el alumno

- Definir un problema y limitar una primera versión.
- Explicar entrada, proceso y salida con un ejemplo.
- Escribir expectativas comprobables antes del código.
- Pedir cambios pequeños y comprender su lógica.
- Ejecutar, comparar esperado y observado y conservar evidencia.
- Decidir si la IA cumplió, no cumplió o dejó algo pendiente.

## Recorrido del material

[README](../../README.md) -> resultado de referencia -> [Apuntes](../../Apuntes.md) -> [HOJA_DE_TRABAJO](../../HOJA_DE_TRABAJO.md) -> [prompts por hito](../../CLASE_OPENCODE_Y_CHAT.md).

[AGENTS.md](../../AGENTS.md) explica en español cómo debe colaborar el agente. El alumno puede usar OpenCode o un chat copiando archivos, con las mismas comprobaciones.

## Dos momentos del proyecto

La referencia existente usa app.py, un CSV local de tweets, Streamlit, Pandas, Plotly y un modelo de pysentimiento. Sus limitaciones están en [estado.md](estado.md).

La reconstrucción del alumno usa una carpeta nueva, comentarios sintéticos, reglas sencillas y app/main.py. Incorpora carga, filtros y descarga por pasos. El modelo real y el despliegue son extensiones.

La primera observación no requiere activar la clasificación real. Ver etiquetas del CSV en un gráfico no significa que el modelo haya generado esas etiquetas durante la sesión.

## Datos y alcance

El CSV local de la referencia no está garantizado por Git. El docente prepara los datos y el entorno antes de mostrar el panel. Para reconstruir, los ejemplos se inventan y no contienen nombres ni usuarios reales.

La primera versión no conecta redes sociales ni exige APIs. Publicar requiere una etapa específica, cuentas y verificaciones propias. No se presentan funcionalidades planeadas como implementadas.
