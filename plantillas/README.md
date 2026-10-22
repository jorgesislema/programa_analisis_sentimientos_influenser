# Plantillas del alumno — recrea tu panel desde cero

Estas cinco plantillas acompañan a [Apuntes.md](../Apuntes.md) y a [HOJA_DE_TRABAJO.md](../HOJA_DE_TRABAJO.md). No son la solución: son las hojas que tú completas para dirigir a la IA.

## Orden de uso

| Plantilla | Cuándo | Para qué |
|---|---|---|
| [1. Prompt del ingeniero](01-prompt-ingeniero.md) | Antes del Hito 0 | La IA acepta guiarte y no decide por ti |
| [2. Estructura](02-estructura.md) | Antes del Hito 1 | Decides qué carpeta y archivo hace cada cosa |
| [3. Archivos](03-archivos.md) | Hitos 1 a 3 | Pides un archivo por vez y lo compruebas |
| [4. Pruebas](04-pruebas.md) | Hito 4 | Defines la evidencia y ejecutas pytest |
| [5. Documentación](05-documentacion.md) | Cierre | Dejas registro de lo construido |

## El ciclo que repites

```text
PAPEL      -> escribo qué debe hacer y cómo lo compruebo
PLAN       -> la IA propone máximo tres pasos
REVISIÓN   -> comparo el plan con mi hoja
CÓDIGO     -> pido un archivo o un hito
EJECUCIÓN  -> abro la app y ejecuto las pruebas
COMPARACIÓN-> anoto esperado, observado y evidencia
DECISIÓN   -> marco cumple, no cumple o pendiente
GUARDADO   -> conservo lo que funciona
```

## Cómo usarlas

1. Completa los espacios en papel o en el editor **antes** de pegar el prompt.
2. Copia solo el bloque de prompt, no todo el documento.
3. Pega tu contexto real: tema, problema y datos.
4. Revisa el plan antes de pedir código.
5. Guarda la evidencia en la plantilla 4 y en la 5.

En **OpenCode**, abre tu carpeta nueva y trabaja ahí. Si no lo tienes instalado, sigue [INSTALACION_OPENCODE.md](../INSTALACION_OPENCODE.md). En **Qwen o DeepSeek**, pega el adaptador de [CLASE_OPENCODE_Y_CHAT.md](../CLASE_OPENCODE_Y_CHAT.md) y copia los archivos completos.

## Reglas

- Los espacios en blanco los completas tú, no la IA.
- Si una plantilla no aplica a tu tema, escribe por qué.
- No presentes datos inventados como comentarios reales.
- No copies el código de la referencia sin entender qué hace.
- Una frase de la IA no reemplaza una prueba ejecutada.
- Si algo no se comprobó, queda **pendiente**.

## Al terminar

Deberías poder responder:

- ¿Qué problema resuelvo y para quién?
- ¿Cómo recorre un comentario mi programa, de la entrada a la pantalla?
- ¿Qué pedí, qué hizo la IA y qué evidencia tengo?
- ¿Qué límite descubrí y qué queda pendiente?
