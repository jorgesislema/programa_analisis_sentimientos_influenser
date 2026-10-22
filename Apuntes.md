# Tu clase: de una idea a un panel que funciona

Hoy vas a **dirigir** la construcción de un panel de comentarios. Tú defines qué debe hacer y compruebas si la IA cumplió. La IA escribe el código.

Ya viste prompts y arquitectura. Hoy no estudiamos teoría: construimos, ejecutamos y verificamos.

## 1. La idea en una frase

> Escribo en papel qué necesito y cómo lo comprobaré. Pido el código. Ejecuto. Comparo lo esperado con lo observado. Decido si cumple.

Una pantalla bonita no basta: los datos, las cuentas y las acciones también deben funcionar.

## 2. Antes de pedir código

Completa [HOJA_DE_TRABAJO.md](HOJA_DE_TRABAJO.md). Después, usa las [plantillas del alumno](plantillas/) para convertir la hoja en pedidos: rol del ingeniero, estructura, archivos, pruebas y documentación.

Como mínimo:

| Pregunta | Ejemplo |
|---|---|
| ¿Qué problema resuelvo? | Hay demasiados comentarios para revisar su tono uno a uno. |
| ¿Qué entra? | Un CSV con `comment_id`, `texto` y `likes` opcional. |
| ¿Qué pasos hay? | Leer, validar, limitar el lote, clasificar por reglas, contar y filtrar. |
| ¿Qué sale? | Tres tarjetas, un gráfico de barras, una tabla y un CSV descargable. |
| ¿Qué queda fuera? | Redes sociales, usuarios reales, API y modelo de IA. |
| ¿Cómo compruebo? | Cuento cinco filas y calculo 40%, 40% y 20%. |

Dibuja la pantalla al reverso. Escribe **tres casos**: uno normal, uno con datos incorrectos y uno al cambiar un filtro.

No uses «que funcione bien». Escribe algo observable: «si filtro Negativo, la tabla muestra solo los dos comentarios negativos».

## 3. Las dos rutas

**OpenCode:** abre tu carpeta nueva, entrega la hoja y el prompt del hito. El agente crea archivos y puede ejecutar. Tú abres la app y revisas.

**Qwen o DeepSeek en el navegador:** pega el adaptador de [los prompts](CLASE_OPENCODE_Y_CHAT.md), copia cada archivo completo en la ruta indicada, guarda y ejecuta los comandos. El chat no ve tu equipo: envíale la salida real.

Las dos rutas valen lo mismo. Copiar código no es hacer trampa; copiar sin comprobar deja el trabajo incompleto.

Si eliges OpenCode y no está instalado, sigue [INSTALACION_OPENCODE.md](INSTALACION_OPENCODE.md), que usa la terminal de VS Code sin permisos de administrador.

## 4. Los cuatro hitos

### Hito 0 — Del papel al plan (10 min)

Entrega tu hoja y pide un plan de **tres pasos**. No escribas código todavía.

Comprueba: ¿el plan respeta tu problema, tu alcance y tu boceto? Si no, corrígelo antes de seguir.

### Hito 1 — Tu primer panel (20 min)

Cinco comentarios inventados dentro del archivo, con etiquetas preparadas. Título, tres tarjetas, barras y tabla.

Comprueba **C01**: cuenta las cinco filas y verifica 2 positivos (40%), 2 negativos (40%) y 1 neutral (20%). Es una cuenta manual, no una predicción de IA.

### Hito 2 — Tus datos entran (20 min)

Los ejemplos pasan a un CSV. La app valida archivo vacío, columna `texto` ausente, filas vacías e ids repetidos.

Comprueba **C02** (un CSV válido muestra sus filas) y **C03** (un CSV sin `texto` muestra ayuda y no rompe).

### Hito 3 — La app decide y responde (25 min)

Clasificación por reglas: listas pequeñas de palabras positivas y negativas. Sin API y sin modelo. Límite de lote, filtros, búsqueda y descarga.

Comprueba:

- **C04:** puedes explicar por qué un texto recibió su etiqueta.
- **C05:** un lote de 10 sobre 20 filas produce exactamente 10 resultados con sus ids.
- **C06:** al filtrar, tarjetas, gráfico y tabla muestran las mismas filas.
- **C07:** el CSV descargado tiene los mismos ids que la tabla.
- **C08:** cambiar de filtro no borra el análisis.
- **C09:** al cargar otro archivo no aparecen resultados del anterior.

### Hito 4 — Comprueba antes de confiar (15 min)

Pide pruebas de: carga válida, archivo sin texto, clasificación por reglas, límite del lote y coherencia al filtrar. Ejecuta `pytest` y lee la salida real.

Comprueba **C10**: un fallo controlado queda como error, **no** como Neutral.

### Cierre — Tu mejora (10 min)

Elige **un** cambio pequeño. Escribe antes qué debe pasar y cómo lo comprobarás. Pídelo después. Comprueba **C12**.

## 5. Tu tabla de verificación

| ID | Esperaba | Observé | Evidencia | Decisión |
|---|---|---|---|---|
| C01 | | | | Cumple / No cumple / Pendiente |
| C02 | | | | |
| C03 | | | | |
| C04 | | | | |
| C05 | | | | |
| C06 | | | | |
| C07 | | | | |
| C08 | | | | |
| C09 | | | | |
| C10 | | | | |
| C12 | | | | |

La evidencia es una cuenta, un archivo, una captura o la salida real de un comando. **La decisión es tuya.**

No cambies tu expectativa solo para que el resultado parezca correcto. Si te equivocaste, explica por qué y anota la corrección.

## 6. Si algo falla

Pide ayuda con este formato:

```text
Comprobaba [criterio]. Esperaba [resultado], pero observé [resultado real].
Para repetirlo hice [pasos]. Este es el mensaje: [pegar sin claves ni datos privados].
Explícame la causa probable y el cambio mínimo. Después dime cómo repetir la comprobación.
```

## 7. Comandos

Desde tu carpeta nueva, en Windows:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app/main.py
```

En otra terminal, para las pruebas:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

La referencia de este repositorio se abre con `app.py`. No mezcles las dos carpetas.

## 8. Entrega

1. Tu hoja y tu boceto, anteriores al código.
2. Tu carpeta con la app y las instrucciones para abrirla.
3. Tu tabla de verificación con evidencias.
4. Una explicación de dos minutos: qué problema resuelves, cómo recorre un comentario tu programa, qué comprobaste y qué queda pendiente.

Al final, responde: **¿qué pediste, qué hizo la IA y cómo comprobaste si cumplió?**
