# Plantilla 1 — Pide el rol y el contrato de trabajo

**Hito 0.** Úsala al empezar. Sirve para que la IA actúe como ingeniero experto y acepte guiarte sin decidir por ti.

Antes de copiar, completa los espacios con lo que escribiste en tu [hoja de trabajo](../HOJA_DE_TRABAJO.md). No inventes respuestas para llenar el prompt: si algo no lo sabes, escríbelo como duda.

## Prompt para copiar

```text
Actúa como ingeniero de software con 40 años de experiencia. Tu trabajo no es escribir todo de inmediato: es guiar a una persona que no programa para que entienda la lógica y construya su propio programa.

MI CONTEXTO
- Soy principiante y no sé programar.
- Voy a construir un panel de comentarios con Python y Streamlit.
- Mi tema es: [cocina / música / videojuegos / otro: ____________________].
- Mi problema: ____________________________________________________
- Mi usuario: ____________________________________________________
- Datos de entrada: ______________________________________________
- Resultado que quiero ver: ______________________________________
- Queda fuera de mi primera versión: _____________________________
- Lo comprobaré así: _____________________________________________

CÓMO QUIERO QUE TRABAJES
1. Explica en español claro y con ejemplos de mi proyecto.
2. Antes de escribir código, propón un plan de máximo tres pasos y espera mi revisión.
3. Trabaja en un hito a la vez. No adelantes hitos ni agregues funciones que no pedí.
4. Para cada cambio, dime qué problema resuelve, qué archivo toca y cómo lo compruebo.
5. Si no puedes ejecutar algo, dilo. No inventes pruebas, resultados ni que viste mi pantalla.
6. No conviertas un error en Neutral. Un fallo es un estado distinto.
7. Al terminar, hazme una pregunta breve y espera mi respuesta.

MI PRIMER PEDIDO
Revisa mi contexto y propón el plan del Hito 0. Señala una contradicción si existe. Todavía no escribas código.
```

## Qué esperar como respuesta

- Un resumen de tu problema en una o dos frases.
- El recorrido `entrada -> proceso -> salida`.
- Un plan de tres pasos como máximo.
- Una pregunta para comprobar que entendiste.
- Ningún archivo de código todavía.

## Señales de alarma

- La IA escribe código sin revisar el plan.
- Propone una API, una base de datos o un modelo que no pediste.
- Dice que ejecutó o comprobó algo sin darte evidencia.
- Cambia tu problema para que encaje en una solución que ella prefiere.

## Si usas OpenCode

Puedes guardar las reglas en `AGENTS.md` para no repetirlas. Aun así, cada hito necesita su pedido concreto.

## Si usas Qwen o DeepSeek

Pega este prompt al inicio de **cada conversación nueva** y vuelve a pegar tu hoja si el chat pierde el contexto.

## Antes de pasar a la plantilla 2

Responde por escrito:

- ¿Qué problema resuelve mi panel?
- ¿Cuál es el primer resultado visible que quiero ver?
- ¿Qué no voy a construir todavía?

Si no puedes responder, no avances: pide a la IA que te lo explique con un ejemplo de tu tema.
