# Plantilla 2 — Diseña la estructura antes de crear archivos

**Antes del Hito 1.** Una carpeta es un lugar; un archivo es un documento; un módulo es un archivo que agrupa funciones con una misma responsabilidad.

No crees archivos al azar. Primero decide **qué hace cada parte** y después pide su contenido.

## Mapa de referencia de la clase

Esta es la estructura de destino. Léela, pero escribe tu propio mapa abajo.

| Ruta | Responsabilidad | Qué contiene | Qué NO contiene |
|---|---|---|---|
| `app/main.py` | Interfaz | Título, tarjetas, gráfico, tabla, filtros y botones | Reglas de clasificación |
| `src/analizador/io.py` | Carga y validación | Leer CSV, revisar columnas, ids y filas vacías | Gráficos ni widgets |
| `src/analizador/metricas.py` | Cálculos | Conteos, porcentajes y filtros | Acceso a Streamlit |
| `src/analizador/sentimiento.py` | Clasificación | Listas de palabras, reglas y límite del lote | Presentación |
| `data/sample/comentarios.csv` | Datos sintéticos | `comment_id`, `texto`, `fecha`, `likes` | Nombres ni datos personales |
| `tests/` | Pruebas | Comprobaciones con pytest | La app abierta en el navegador |
| `docs/` | Documentación | Hoja, diccionario, decisiones y verificación | Código |

## Tu mapa

Completa una fila por cada parte que vas a crear. Si una no la necesitas todavía, déjala para después.

| Ruta | ¿Qué responsabilidad tiene? | ¿Qué recibe? | ¿Qué devuelve? | ¿Qué NO debe hacer? |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

## Dibuja tu árbol

Completa los nombres y las rutas. Usa `____` para lo que aún no decidas.

```text
mi-panel/
  app/
    ______.py          -> ________________________________
  src/
    ______/
      __init__.py      -> ________________________________
      ______.py        -> ________________________________
      ______.py        -> ________________________________
      ______.py        -> ________________________________
  data/
    sample/
      ______.csv       -> ________________________________
  tests/
    ______.py          -> ________________________________
  docs/
    ______.md          -> ________________________________
  README.md            -> ________________________________
  requirements.txt     -> ________________________________
```

## Pide una revisión, no la creación

```text
Revisa la estructura que escribí. Todavía no crees archivos.
Dime:
1. Qué responsabilidad tiene cada archivo.
2. Si algún archivo mezcla dos responsabilidades.
3. Si falta o sobra algo para el primer panel.
4. Una pregunta para que yo explique la estructura con mis palabras.
No agregues carpetas ni dependencias que no estén en mi mapa.
```

## Reglas simples

- Una responsabilidad por archivo.
- La interfaz no clasifica; solo muestra lo que recibe.
- La clasificación no dibuja gráficos.
- Los datos de ejemplo viven en `data/`, no dentro del código de la interfaz.
- Las pruebas viven en `tests/`, no al final de `app/main.py`.
- No crees una carpeta por cada idea: solo por una responsabilidad que puedas explicar.

## Antes de pasar a la plantilla 3

- Puedes explicar en una frase qué hace cada carpeta.
- Sabes qué archivo crearás primero.
- Sabes qué archivo **no** vas a crear todavía.
