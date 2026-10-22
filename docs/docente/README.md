# Material del docente

Esta carpeta conserva la versión extensa. El alumno no necesita leerla para la sesión de dos horas.

| Archivo | Uso |
|---|---|
| [clase_desarrollar_programa_con_ia.md](clase_desarrollar_programa_con_ia.md) | Guía completa, criterios C01–C12 y rúbrica |
| [CURSO_PROMPTS.md](CURSO_PROMPTS.md) | Diagnóstico del repositorio y ruta extensa de ampliación |
| [arquitectura.md](arquitectura.md) | Recorrido de un comentario en la referencia |
| [context.md](context.md) | Para quién es el curso y qué debe aprender |
| [estado.md](estado.md) | Comprobaciones y limitaciones conocidas |

## Qué cambió en la versión de 2 horas

- El root quedó para el alumno: `README.md`, `Apuntes.md`, `HOJA_DE_TRABAJO.md`, `CLASE_OPENCODE_Y_CHAT.md`, `AGENTS.md` y `plantillas/`.
- La sesión se redujo a **cuatro hitos** más plan y cierre.
- Fechas y tendencia temporal (C11), modelo real, GitHub y publicación pasan a una segunda sesión.
- No se modificó `app.py`, `src/` ni `tests/`: sigue siendo la referencia del docente.

## Cómo compartir el material

No entregues la carpeta completa. Quedan dentro `.venv/`, `.git/`, `__pycache__/`, `.coverage` y configuraciones del agente que el alumno no necesita. Comparte solo lo versionado o un ZIP con `README.md`, `Apuntes.md`, `HOJA_DE_TRABAJO.md`, `CLASE_OPENCODE_Y_CHAT.md`, `AGENTS.md`, `app.py`, `src/`, `tests/` y el CSV de referencia.

La skill de Streamlit en inglés vivía en `.agents/` y `.claude/` como enlaces a `.venv/`. Se eliminaron del proyecto: no es material del curso y confunde a quien no programa. Si hace falta, el agente usa `AGENTS.md` en español.

## Antes de clase

1. Comprueba que el panel de referencia abre con el CSV local.
2. Prueba OpenCode o el chat alternativo con la cuenta que usará el grupo.
3. Ejecuta una vez la app con el punto de recuperación del hito 1.
4. Ten a mano la salida de `pytest` de datos y gráficos.
5. Decide dónde creará cada alumno su carpeta nueva.
