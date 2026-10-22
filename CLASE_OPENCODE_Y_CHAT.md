# Prompts listos para copiar — sesión de 2 horas

Usa este archivo en orden. Cada hito tiene un prompt para **OpenCode** y otro para **Qwen o DeepSeek**. Antes de cada prompt, escribe tu expectativa:

```text
Mi criterio es [C01, C02...].
En papel escribí: [comportamiento].
Con estos datos: [ejemplo].
Espero observar: [resultado concreto].
Lo comprobaré así: [acción, cuenta o prueba].
No cambies mi expectativa para adaptarla al resultado; dime si está mal y por qué.
```

## 1. Adaptador para chat (pegar una vez)

```text
No sé programar. Voy a copiar tus archivos en mi computadora y no tienes acceso a ella.
No afirmes que guardaste, ejecutaste o comprobaste algo.

Trabajamos en una carpeta nueva, no dentro del repositorio de referencia.
Para cada archivo indica la ruta, si debo crearlo o reemplazarlo y su contenido completo.
No uses fragmentos, «el resto igual» ni parches diff. Separa los comandos del código.
Entrega como máximo dos archivos por respuesta y espera mi «listo».
Dame un comando por vez para Windows con .\.venv\Scripts\python.exe.

Stack: Python, Streamlit, Pandas, Plotly y pytest. Sin API, sin modelo y sin dependencias nuevas.
La app se abre con: .\.venv\Scripts\python.exe -m streamlit run app/main.py
Las pruebas se ejecutan con: .\.venv\Scripts\python.exe -m pytest -q

Trabaja solo en el hito que te pida. Al terminar, dime qué debo observar y hazme una pregunta breve.
```

## 2. AGENTS.md para tu carpeta (opcional en OpenCode)

Crea `AGENTS.md` en tu carpeta con este contenido:

```markdown
# Proyecto de clase: Vibe Check
Somos principiantes. Explica en español y con pasos pequeños.
Stack: Python, Streamlit, Pandas, Plotly, pytest. Sin API ni modelo de IA.
Interfaz: app/main.py. Lógica: src/analizador/io.py, metricas.py, sentimiento.py.
Trabaja solo en el hito pedido. Antes, propón tres pasos y espera mi revisión.
Ejecuta las pruebas y reporta la salida real. Si no puedes, dilo.
No conviertas errores en Neutral ni inventes resultados. Solo datos sintéticos.
Al terminar, di qué debo observar y hazme una pregunta breve.
```

## 3. Hito 0 — Del papel al plan (10 min)

```text
Eres mi tutor en una clase para no programadores. Construiremos Vibe Check con Python y Streamlit para explorar comentarios sintéticos. La app clasifica con reglas, no con un modelo de IA.

Esta es mi hoja de papel:
[pegar las respuestas y el boceto]

Resume el problema y el flujo entrada -> proceso -> salida. Señala una contradicción si existe y propón un plan de solo tres pasos para la primera pantalla. No escribas código todavía. Dime qué debería comprobar y hazme una pregunta.
```

Después de revisar el plan: «Implementa el hito 1 con este plan».

## 4. Hito 1 — Primer panel (20 min)

```text
Crea solo app/main.py. Usa cinco comentarios sintéticos dentro del archivo, con etiquetas preparadas: dos Positivo, dos Negativo y uno Neutral. No uses un clasificador todavía.
Muestra el aviso: «Ejemplos preparados: todavía no se ha ejecutado un clasificador».
Incluye un título propio, tres tarjetas (Positivo, Negativo, Neutral) con cantidad y porcentaje, un gráfico de barras con etiquetas y una tabla con comment_id, texto y sentimiento.
Usa Streamlit, Pandas y Plotly. Sin CSS interno, sin API y sin archivos externos. Los porcentajes deben ser 40%, 40% y 20%.
Al final, pídeme contar las cinco filas y comprobar los porcentajes a mano.
```

**C01:** cuenta 5 filas: 2 positivas (40%), 2 negativas (40%), 1 neutral (20%).

### Punto de recuperación del hito 1

Si el chat se bloquea, el docente puede entregar este archivo completo. El alumno lo ejecuta y continúa.

```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Vibe Check", page_icon="💬", layout="wide")

COMENTARIOS = [
    {"comment_id": "c01", "texto": "Excelente receta, gracias", "sentimiento": "Positivo"},
    {"comment_id": "c02", "texto": "Me encanta este video", "sentimiento": "Positivo"},
    {"comment_id": "c03", "texto": "El sonido es horrible", "sentimiento": "Negativo"},
    {"comment_id": "c04", "texto": "La explicación es confusa", "sentimiento": "Negativo"},
    {"comment_id": "c05", "texto": "El video dura diez minutos", "sentimiento": "Neutral"},
]

df = pd.DataFrame(COMENTARIOS)
conteo = df["sentimiento"].value_counts()
total = len(df)

st.title("Vibe Check")
st.caption("Ejemplos preparados: todavía no se ha ejecutado un clasificador.")

c1, c2, c3 = st.columns(3)
c1.metric("Positivos", int(conteo.get("Positivo", 0)), f"{conteo.get('Positivo', 0) / total:.0%}")
c2.metric("Negativos", int(conteo.get("Negativo", 0)), f"{conteo.get('Negativo', 0) / total:.0%}")
c3.metric("Neutrales", int(conteo.get("Neutral", 0)), f"{conteo.get('Neutral', 0) / total:.0%}")

datos_grafico = (
    conteo.rename_axis("Sentimiento").reset_index(name="Cantidad")
)
fig = px.bar(datos_grafico, x="Sentimiento", y="Cantidad", text="Cantidad")
st.plotly_chart(fig, use_container_width=True)

st.dataframe(df[["comment_id", "texto", "sentimiento"]], use_container_width=True)
```

## 5. Hito 2 — Datos y validación (20 min)

```text
Conserva el panel. Separa la carga y las métricas en src/analizador/io.py y src/analizador/metricas.py, con __init__.py. app/main.py queda como interfaz.
Crea data/sample/comentarios.csv con 20 comentarios sintéticos: comment_id único, texto, fecha ISO y likes. La app carga ese archivo al iniciar y permite subir otro CSV.
Valida: archivo vacío, columna texto ausente, filas con texto vacío e ids duplicados. Informa cuántas filas se aceptaron y rechazaron. No inventes fechas ni likes faltantes.
Si falta comment_id, genera ids estables para esa carga y aclara que no identifican personas.
Mantén visible el aviso de que las etiquetas todavía no se calculan.
Asegura que el comando funcione desde la raíz con python -m streamlit run app/main.py, sin PYTHONPATH manual. Si el import de src/ falla, crea src/__init__.py y explica por qué.
Incluye una prueba de carga válida y otra de columna texto ausente. Ejecútalas y muéstrame la salida real.
```

**C02:** un CSV válido muestra sus filas.
**C03:** un CSV sin `texto` muestra un mensaje claro y no rompe la app.

## 6. Hito 3 — Reglas, lote, filtros y descarga (25 min)

```text
Implementa en src/analizador/sentimiento.py un clasificador por reglas. Usa listas pequeñas de palabras positivas y negativas declaradas en el código.
Normaliza a minúsculas y quita puntuación. Compara palabras completas. Si hay empate, devuelve Neutral. Devuelve Positivo, Negativo o Neutral.
Una excepción de procesamiento debe devolver estado «error» y sentimiento vacío; nunca Neutral.
Sustituye las etiquetas preparadas por el resultado calculado e identifica el motor como «Clasificación por reglas, no modelo de IA».
Limita el lote a 10 comentarios antes de clasificar y conserva los resultados por comment_id en st.session_state. Al cambiar un filtro no vuelvas a clasificar ni borres resultados. Al cargar otro archivo, no muestres el análisis anterior como actual.
Añade filtros de sentimiento y búsqueda literal, y una descarga CSV con las mismas filas visibles. Las tarjetas, el gráfico y la tabla deben usar ese mismo conjunto.
Incluye una pestaña «Cómo funciona» con un ejemplo y un límite (negación o sarcasmo).
Ejecuta las pruebas y muéstrame la salida real. Pídeme que compruebe un filtro y la descarga.
```

**C04:** explicas la regla de una etiqueta.
**C05:** 10 de 20 producen 10 resultados con sus ids.
**C06:** filtro, tarjetas, gráfico y tabla coinciden.
**C07:** descarga y tabla tienen los mismos ids.
**C08:** filtrar conserva el análisis.
**C09:** otro archivo no reutiliza resultados viejos.

## 7. Hito 4 — Pruebas y errores (15 min)

```text
Revisa los criterios C01–C09 y escribe pruebas de comportamiento: carga válida, archivo sin texto, filas vacías informadas, ids duplicados, clasificación positiva, negativa y empate, y lote de 20 limitado a 10.
Añade una prueba que provoque un fallo de clasificación y compruebe que queda como error, sin aumentar Neutral.
Ejecuta: .\.venv\Scripts\python.exe -m pytest -q
Reporta solo la salida real. Si falla algo, explica esperado, observado, causa y corrección mínima. No cambies una expectativa correcta para hacer pasar la prueba.
Después pídeme una comprobación manual: forzar un error, revisar que no cuenta como Neutral y volver a filtrar.
```

**C10:** el error queda separado de Neutral.

## 8. Cierre — Mejora propia (10 min)

```text
Quiero añadir una sola mejora: [mi propuesta].
Antes de programar, ayúdame a escribir qué debe pasar y cómo lo comprobaré. Implementa el cambio mínimo después de revisar ese comportamiento. Conserva el panel y las pruebas.
Actualiza README.md con los comandos reales.
Hazme tres preguntas, una por vez, y espera mi respuesta: qué problema resuelvo, cómo recorre un comentario el programa y qué comprobé.
```

**C12:** ocurre tu cambio sin romper lo anterior.

## 9. Comandos de la carpeta nueva

```powershell
.\.venv\Scripts\python.exe -m streamlit run app/main.py
```

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Si el chat o el agente afirma que ejecutó algo, pide la salida real. Sin salida en tu equipo no hay evidencia.

## 10. Fuera de esta sesión

Fechas y tendencia temporal (C11), modelo real, evaluación con más comentarios, GitHub y publicación. Se retoman en la segunda sesión con la guía extensa de [docs/docente/](docs/docente/).
