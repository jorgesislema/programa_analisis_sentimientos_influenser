# Plantilla 3 — Pide el contenido de cada archivo

**Hitos 1 a 3.** Pide **un archivo por vez** y compruébalo antes de seguir. Un archivo completo y probado vale más que cinco a medias.

## Ficha antes de pedir un archivo

Completa esta ficha por cada archivo. Si no puedes llenar entrada, proceso y salida, todavía no pidas código.

```text
Archivo: ________________________________________________
Hito: ____   Criterio: ____
¿Crear o reemplazar?: ___________________________________
Entrada (qué recibe): ___________________________________
Proceso (pasos en orden): _______________________________
Salida (qué devuelve o muestra): ________________________
Lo que NO debe hacer: ___________________________________
Cómo lo comprobaré: _____________________________________
```

## Prompt para copiar

```text
Crea o reemplaza solo este archivo: [ruta completa]

Entrada: ________________________________________________
Proceso: ________________________________________________
Salida: _________________________________________________
Lo que NO debe hacer: ___________________________________
Criterio de la clase: [C01, C02, C03...]

Reglas:
- Entrega el archivo completo, sin fragmentos ni «el resto igual».
- No agregues dependencias, APIs ni archivos que no pedí.
- Explica en español qué hace cada parte importante.
- Al final dime cómo comprobarlo y qué debo observar.
- No afirmes que ejecutaste o comprobaste algo si no tienes mi salida real.
```

En OpenCode puedes pedir varios archivos del mismo hito. En un chat, pide **como máximo dos** y espera a guardarlos antes de continuar.

## Seguimiento de archivos

| Archivo | Hito | ¿Creado? | ¿Ejecutado? | Evidencia | Pendiente |
|---|---|---|---|---|---|
| `app/main.py` | 1 | | | | |
| `data/sample/comentarios.csv` | 2 | | | | |
| `src/analizador/io.py` | 2 | | | | |
| `src/analizador/metricas.py` | 2 | | | | |
| `src/analizador/sentimiento.py` | 3 | | | | |
| `tests/______.py` | 4 | | | | |
| `docs/______.md` | 5 | | | | |

## Orden recomendado

1. `app/main.py` con cinco comentarios y etiquetas preparadas.
2. `data/sample/comentarios.csv` con veinte comentarios sintéticos.
3. `src/analizador/io.py` para cargar y validar.
4. `src/analizador/metricas.py` para contar y filtrar.
5. `src/analizador/sentimiento.py` para clasificar por reglas.
6. `tests/` para comprobar lo anterior.
7. `docs/` para dejar registro.

## Qué revisar cuando llegue el archivo

- ¿Está completo o tiene huecos como `...` o «aquí va tu código»?
- ¿Usa las rutas y nombres que acordamos?
- ¿Hace solo lo que pedí?
- ¿Puedo explicar qué recibe, qué decide y qué devuelve?
- ¿La app sigue abriendo después del cambio?

## Punto de retorno

Cuando un hito funcione y lo hayas comprobado:

- Copia la carpeta con otro nombre, o
- Crea un commit local si Git está disponible.

Así puedes volver atrás si el siguiente cambio rompe lo que ya funcionaba.

## Ejemplo completo (modelo)

Esta ficha está llena para que veas el nivel de detalle esperado. Es un modelo de **cómo pensar**, no una orden para copiar el archivo.

```text
Archivo: src/analizador/io.py
Hito: 2   Criterio: C02 y C03
¿Crear o reemplazar?: Crear

Entrada:
- Una ruta a un CSV o un archivo subido por el usuario.
- Columnas esperadas: comment_id, texto, fecha, likes.

Proceso:
1. Leer el CSV con pandas.
2. Comprobar que existe la columna obligatoria texto.
3. Quitar filas con texto vacío e informar cuántas se rechazaron.
4. Revisar ids duplicados e informarlos sin mezclar resultados.
5. Si falta comment_id, generar uno estable para esa carga.

Salida:
- Una tabla válida para el resto de la app.
- Un resumen con filas aceptadas, rechazadas y errores.

Lo que NO debe hacer:
- No dibuja gráficos ni usa Streamlit.
- No clasifica sentimiento.
- No inventa fechas ni likes faltantes.

Cómo lo comprobaré:
- Cargo un CSV válido y veo sus filas.
- Cargo un CSV sin la columna texto y aparece un mensaje claro, sin romper la app.
```

### El mismo ejemplo convertido en pedido

```text
Crea solo src/analizador/io.py.

Entrada: una ruta a un CSV o un archivo subido con las columnas comment_id, texto, fecha y likes.
Proceso: leer con pandas, comprobar la columna texto, quitar filas vacías e informar cuántas, revisar ids duplicados y generar comment_id estable si falta.
Salida: una tabla válida y un resumen con aceptadas, rechazadas y errores.
No debe: dibujar gráficos, usar Streamlit, clasificar sentimiento ni inventar fechas o likes.
Criterio: C02 y C03.

Entrega el archivo completo y explica cómo comprobarlo con un CSV válido y otro sin texto.
```

Fíjate en la diferencia: la ficha describe **qué necesitas**; el prompt pide **un archivo concreto**. Ninguno de los dos decide por ti si el resultado cumple.

## Antes de pasar a la plantilla 4

- Cada archivo del hito está guardado en la ruta correcta.
- La app abre y muestra lo que pediste.
- Anotaste qué comprobaste y con qué evidencia.
- Puedes explicar un archivo sin leerlo entero.
