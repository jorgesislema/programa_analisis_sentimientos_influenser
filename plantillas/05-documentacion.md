# Plantilla 5 — Documenta lo que construiste

**Cierre.** La documentación no es decoración: permite que otra persona abra tu programa y que tú recuerdes por qué tomaste cada decisión.

Crea estos archivos dentro de tu carpeta:

```text
README.md
docs/
  00-hoja-de-papel.md
  diccionario-de-datos.md
  decisiones.md
  verificacion.md
```

## 1. `README.md`

Completa:

```markdown
# Nombre de mi panel

Qué problema resuelve: ______________________________________

Para quién es: ______________________________________________

Qué datos usa: ______________________________________________

Cómo se abre:

    .\.venv\Scripts\python.exe -m streamlit run app/main.py

Qué debe hacer:
- ___________________________________________________________
- ___________________________________________________________
- ___________________________________________________________

Qué NO hace todavía:
- ___________________________________________________________

Cómo se comprueba:
- ___________________________________________________________
```

## 2. `docs/00-hoja-de-papel.md`

Transcribe tu hoja, no la reescribas para que coincida con el resultado.

| Pregunta | Mi respuesta original |
|---|---|
| ¿Qué problema resuelvo? | |
| ¿Quién lo tiene y cómo lo resuelve hoy? | |
| ¿Qué solución propongo? | |
| ¿Qué entra, qué pasos hay y qué sale? | |
| ¿Qué debe hacer mi primera versión? | |
| ¿Qué queda fuera? | |
| ¿Qué espero ver cuando funcione? | |
| ¿Cómo comprobaré que cumplió? | |

Si corregiste una expectativa, escribe el motivo y la fecha.

## 3. `docs/diccionario-de-datos.md`

| Columna | Obligatoria | Tipo | Qué significa | Qué hago si falta o es inválida |
|---|---|---|---|---|
| `comment_id` | | | | |
| `texto` | | | | |
| `fecha` | | | | |
| `likes` | | | | |

Aclara que `comment_id` identifica un comentario, no a una persona.

## 4. `docs/decisiones.md`

| Decisión | Opciones que consideré | Elegí | Por qué | Cómo lo comprobé |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

Ejemplos de decisión: clasificar con reglas en vez de un modelo; limitar el lote a diez; separar error de Neutral.

## 5. `docs/verificacion.md`

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

La evidencia es una cuenta, un archivo, una captura o la salida real de un comando. Lo no ejecutado queda **pendiente**.

## Prompt para copiar

```text
Ayúdame a completar la documentación sin inventar resultados.

Te entrego:
- Mi hoja de papel: ______________________________________
- Mis archivos actuales: ________________________________
- Mi salida real de pruebas: ____________________________
- Mis decisiones: _______________________________________

Actualiza README.md y docs/ con lo que realmente existe.
No escribas que una prueba pasó si no tengo salida real.
No decidas por mí si un criterio cumple: deja la decisión en mi tabla.
Marca como pendiente lo que no comprobé.
Al final, hazme tres preguntas, una por vez: qué problema resuelvo, cómo recorre un comentario mi programa y qué comprobé.
```

## Checklist de cierre

- [ ] Otra persona puede abrir la app siguiendo el README.
- [ ] La hoja original y las correcciones están separadas.
- [ ] El diccionario explica cada columna.
- [ ] Hay al menos dos decisiones con su motivo.
- [ ] Cada criterio tiene evidencia o dice pendiente.
- [ ] La app indica que clasifica por reglas, no con un modelo.
- [ ] Un error no aparece como Neutral.
- [ ] Sé explicar qué pedí, qué hizo la IA y cómo lo comprobé.
