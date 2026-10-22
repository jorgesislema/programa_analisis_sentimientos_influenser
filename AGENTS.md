# Instrucciones para trabajar con IA en Vibe Check

## Propósito del repositorio

Este repositorio es material de un curso para personas sin experiencia en programación. Primero se observa el resultado de referencia; después el alumno define en papel su propia solución y la reconstruye con ayuda de IA. El objetivo es comprender la lógica y verificar si el programa cumple lo pedido.

Lee README.md para ubicarte y Apuntes.md para seguir la experiencia del alumno. La guía docente está en `docs/docente/clase_desarrollar_programa_con_ia.md`. CLASE_OPENCODE_Y_CHAT.md contiene los prompts por hito y `docs/docente/CURSO_PROMPTS.md` conserva el diagnóstico y ampliaciones.

## Idioma y explicaciones

- Comunícate en español claro. Escribe en español los documentos, mensajes de interfaz y comentarios nuevos; conserva los identificadores de las herramientas y bibliotecas.
- Explica cada concepto necesario con un ejemplo del proyecto. Presenta primero qué problema resuelve un cambio y cómo comprobarlo.
- Usa entrada, proceso y salida para explicar la lógica. Define función, condición, repetición, variable y prueba cuando aparezcan.
- No des por hecho que el alumno sabe crear archivos, usar la terminal, interpretar un error o distinguir una carpeta de un archivo.

## La hoja de papel dirige el trabajo

1. Antes de construir un hito, pide las expectativas que el alumno escribió: problema, comportamiento, entrada de ejemplo, salida esperada y forma de comprobarla. Si ya las proporcionó en la conversación o en sus documentos, úsalas sin volver a solicitarlas.
2. Compara el plan con esas expectativas. Si falta algo indispensable, pregunta solo por ello; no impongas un cuestionario repetido.
3. Implementa el hito acordado mediante cambios pequeños. La autorización para ese hito incluye sus comprobaciones rutinarias; no solicites aprobación por cada archivo o comando.
4. Ejecuta las pruebas pertinentes cuando dispongas de herramientas e indica exactamente qué verificaste. Si no pudiste comprobar algo, márcalo pendiente.
5. Ayuda a reunir la evidencia: esperado, observado y comprobación ejecutada. **El alumno decide si cumple, no cumple o queda pendiente.** No inventes su respuesta ni reemplaces su hoja por una solución escrita por ti.
6. No modifiques una expectativa correcta para hacer coincidir el resultado. Si el criterio es incorrecto o cambió la necesidad, explica el motivo y registra la revisión antes de volver a comprobar.
7. Termina el hito con una pregunta breve sobre su lógica, sin responderla por el alumno. Si el alumno solicita una tarea más amplia, respeta ese alcance y no impongas pausas artificiales.

## Referencia existente y reconstrucción del alumno

- El programa existente se ejecuta con `python -m streamlit run app.py`. Sus módulos son `src/datos.py`, `src/analizador.py` y `src/graficos.py`.
- Ese código usa pysentimiento, no Gemini. El CSV local esperado es `data/sentiment_analysis_dataset.csv`; no es un archivo garantizado por Git. Hay limitaciones registradas en `docs/docente/estado.md`.
- La reconstrucción educativa se hace en **otra carpeta**, con los ejemplos sintéticos y el destino `app/main.py` de CLASE_OPENCODE_Y_CHAT.md. Empieza con reglas y categorías Positivo, Negativo y Neutral, sin API obligatoria.
- No confundas funciones planeadas con funciones existentes. No reestructures el repositorio de referencia para hacer un ejercicio del alumno sin que ese cambio forme parte del pedido.
- No copies automáticamente el código completo al proyecto del alumno: ayuda a construir y comprobar cada hito solicitado. Consultar el código de referencia está permitido; debe explicar qué entiende y qué probará.

## Verificación y datos

- Los ejemplos de clase son sintéticos y deben identificarse como tales. No los presentes como comentarios obtenidos de una red social ni como predicciones de un modelo si son etiquetas preparadas.
- Mantén separados sentimiento, emoción y error de procesamiento. Un fallo no es un resultado Neutral.
- Conserva la relación entre comentario y resultado mediante identificadores. Limita el lote antes de clasificar y comprueba que cantidades y filas coincidan.
- Usa el mismo conjunto visible para indicadores, gráficos, tabla y descarga en la reconstrucción. No presentes posición de filas como tiempo.
- No leas, imprimas ni publiques secretos, contraseñas, `.env` o datos personales. Usa solo los datos necesarios para la tarea.
- No llames APIs ni descargues modelos en pruebas automáticas de la ruta inicial. Usa ejemplos controlados y separa las comprobaciones reales del modelo.
- La primera ejecución de un modelo local puede requerir descargas. No prometas ausencia de internet o de registro para herramientas que no hayas comprobado.
- No introduzcas servicios, claves, frameworks o dependencias adicionales sin una necesidad concreta del hito.
- No ejecutes pruebas de forma repetitiva si ya pasaron y no hubo cambios ni nuevas dudas que lo justifiquen.

## Comandos y alcance de las pruebas actuales

En Windows, si existe el entorno preparado, usa `.\.venv\Scripts\python.exe` en lugar de `python`. Desde la raíz real del repositorio, donde está app.py:

```text
python -m streamlit run app.py
python -m pytest tests/test_datos.py tests/test_graficos.py -q
```

La prueba actual de clasificación puede cargar el modelo. No afirmes que las pruebas de datos y gráficos verifican el modelo o la interfaz completa. Corrige o añade pruebas de comportamiento cuando cambies lógica; para documentación, revisa enlaces, comandos y coherencia sin ejecutar innecesariamente el modelo.

## OpenCode y chat de copiar y pegar

En un agente con acceso al proyecto, lee los archivos necesarios y usa tus herramientas. En un chat sin acceso al equipo, entrega rutas y archivos completos en tandas pequeñas, separa comandos de código y pide la salida real. No afirmes que guardaste, ejecutaste o viste algo sin tener esa capacidad.

No prometas modelos gratuitos permanentes ni acceso sin cuenta. Si falla el acceso, conserva la tarea y propone la alternativa de aula acordada. No publiques una app, envíes datos a un proveedor ni envíes mensajes a otras personas sin la autorización correspondiente.
