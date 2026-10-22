# Plantilla 4 — Define y ejecuta las pruebas

**Hito 4.** Una prueba es un ejemplo que ejecutas y comparas con lo que esperabas. No es una frase de la IA diciendo «funciona».

Hay dos comprobaciones distintas:

| Comprobación | Pregunta | Ejemplo |
|---|---|---|
| Del programa | ¿Hace la acción que pedí? | Un CSV sin `texto` muestra ayuda y no rompe la app. |
| De la clasificación | ¿La etiqueta parece razonable? | Un comentario con «no me gusta» recibe Negativo o Neutral. |

Una prueba del programa no demuestra que el clasificador entienda el sarcasmo.

## Ficha de una prueba

```text
Nombre: ________________________________________________
Criterio: ____
Dado (entrada): _________________________________________
Cuando (acción): ________________________________________
Entonces (resultado esperado): ___________________________
Archivo de prueba: ______________________________________
Cómo lo ejecuto: ________________________________________
```

## Tabla de verificación

Completa la evidencia **después** de ejecutar. No la escribas antes de ver el resultado.

| ID | Qué provoco | Qué espero | Evidencia real | Decisión |
|---|---|---|---|---|
| C01 cinco filas y 40/40/20 | | | | Cumple / No cumple / Pendiente |
| C02 CSV válido | | | | |
| C03 CSV sin texto | | | | |
| C04 regla explicable | | | | |
| C05 lote de 10 con sus ids | | | | |
| C06 filtro y conteos | | | | |
| C07 descarga y tabla | | | | |
| C08 análisis conservado | | | | |
| C09 cambio de archivo | | | | |
| C10 error distinto de Neutral | | | | |
| C12 mi mejora | | | | |

## Prompt para copiar

```text
Escribe pruebas de comportamiento para estos criterios: [C0__ y C0__].

Casos que deben cubrir:
- ______________________________________________________
- ______________________________________________________
- ______________________________________________________

Reglas:
- No escribas pruebas que solo comprueben que una función existe.
- Usa datos pequeños y controlados; no dependas de internet.
- Para un fallo de clasificación, comprueba que queda como error y NO como Neutral.
- Ejecuta: .\.venv\Scripts\python.exe -m pytest -q
- Muéstrame la salida real. Si no puedes ejecutar, dame el comando exacto.
- Si una prueba falla, explica esperado, observado, causa probable y cambio mínimo.
- No cambies una expectativa correcta para que la prueba pase.
```

## Comandos

Desde tu carpeta del proyecto, en Windows:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Para una sola prueba:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_mi_prueba.py -q
```

## Pega aquí la salida real

```text
_____________________________________________________________
_____________________________________________________________
_____________________________________________________________
```

## Si una prueba falla

1. Guarda el mensaje completo.
2. Anota qué esperabas y qué ocurrió.
3. Comprueba si el error está en el código, en los datos o en tu expectativa.
4. Pide el cambio mínimo; no reconstruyas todo.
5. Vuelve a ejecutar la misma prueba.
6. Registra la decisión final: cumple, no cumple o pendiente.

## Antes de pasar a la plantilla 5

- Ejecutaste al menos una prueba y tienes su salida real.
- Sabes qué fallo detectaría esa prueba.
- Distingues un error del programa de una etiqueta discutible.
- No confundiste «pytest aprobó» con «la IA clasifica bien».
