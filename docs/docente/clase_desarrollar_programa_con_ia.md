# Clase práctica — Cómo desarrollar un programa con IA: del papel al panel

Proyecto: **Vibe Check**, un panel de comentarios con Python y Streamlit. Material para estudiantes sin experiencia en programación y guía para el docente. Actualizado el 22 de octubre de 2026.

> **Versión de 2 horas.** Este documento conserva la guía extensa. Para la sesión única usa la ruta corta de [CLASE_ALUMNO.md](../../CLASE_ALUMNO.md) y [CLASE_OPENCODE_Y_CHAT.md](../../CLASE_OPENCODE_Y_CHAT.md): cuatro hitos, sin C11 ni publicación. El plan de la sección 7 es la versión larga.

## La idea que guía toda la clase

**Primero escribo en papel qué necesito y cómo lo comprobaré. Después se lo pido a la IA. Finalmente ejecuto el programa y comparo lo que hizo con lo que yo había escrito.**

La IA escribe código y puede equivocarse. El alumno decide el problema, revisa la propuesta y reúne evidencias de que el resultado cumple lo pedido. Una pantalla bonita es parte de la entrega; los datos y las acciones también deben funcionar.

No necesitas escribir código por tu cuenta para participar. Sí necesitas observar, hacer una cuenta sencilla, explicar lo que esperabas y decir cuándo el resultado no cumple.

## 1. Qué vamos a construir y qué material usar

Una persona que crea contenido recibe muchos comentarios y quiere explorar su tono sin leerlos todos de una vez. Construiremos un panel con ejemplos sintéticos, indicadores, gráficos, filtros y descarga. El alumno puede elegir el tema: cocina, música, videojuegos u otro de su interés.

La aplicación inicial clasifica por reglas sencillas. **Usar IA para programar y usar un modelo de IA dentro del programa son cosas diferentes.** Hoy la IA nos ayuda a construir; un modelo preentrenado o una API pueden incorporarse después. La app debe decir qué método está utilizando.

Los documentos se usan juntos:

- **Esta clase:** qué pensar en papel, qué aprender y cómo comprobar el trabajo.
- [CLASE_OPENCODE_Y_CHAT.md](../../CLASE_OPENCODE_Y_CHAT.md): preparación, guion de dos horas y prompts por hito para OpenCode o chat.
- [CURSO_PROMPTS.md](CURSO_PROMPTS.md): diagnóstico del repositorio y ampliaciones para sesiones posteriores. Su ruta extensa se adapta al alcance de esta clase.

### Diferencia entre el repositorio actual y la versión de clase

El código revisado arranca con `app.py`, usa `src/datos.py`, `src/analizador.py` y `src/graficos.py`, carga un CSV local de tweets y utiliza pysentimiento. La documentación de ese código todavía menciona Gemini. La revisión detectó problemas pendientes, como asignar un lote de resultados a una tabla con más filas y tratar fallos del modelo como Neutral.

La versión de clase se construye **en una carpeta nueva**, con datos sintéticos, clasificación por reglas y el punto de entrada `app/main.py` descrito en el complemento. Esa estructura es el destino educativo, no una descripción de archivos ya implementados en el repositorio actual.

No se incluye ni se ha comprobado aquí el ZIP de referencia mencionado en la versión anterior de la clase. La revisión previa ejecutó 15 pruebas de datos y gráficos del repositorio actual, con 92% de cobertura de esos dos módulos; eso no verifica el modelo, la nueva app educativa ni su despliegue.

## 2. La hoja de papel: antes de abrir la IA

Dedica diez minutos a responder a mano. La IA podrá ayudarte a revisar lo escrito después, pero no debe sustituir tu primera definición.

| # | Pregunta | Ejemplo para Vibe Check |
|---|---|---|
| 1 | ¿Cuál es el problema? | Hay demasiados comentarios para revisar su tono uno por uno. |
| 2 | ¿Quién lo tiene y cómo lo resuelve hoy? | La persona que crea contenido los lee manualmente. |
| 3 | ¿Qué solución propongo? | Un panel que resume y permite explorar comentarios. |
| 4 | ¿Cómo funcionará: entrada, proceso y salida? | CSV sintético -> validar y clasificar -> indicadores, gráficos, tabla y descarga. |
| 5 | ¿Qué debe hacer? | Cargar ejemplos, aceptar un CSV, clasificar, filtrar y descargar. |
| 6 | ¿Qué queda fuera? | Acceso a redes, datos personales, cuentas de usuarios, API y entrenamiento en la primera clase. |
| 7 | ¿Qué resultado espero ver? | Un panel legible con cantidades comprobables y comentarios relacionados con cada etiqueta. |
| 8 | ¿Cómo sabré si cumplió? | Haré una cuenta manual, probaré filtros y errores, y compararé tabla y descarga. |

Al reverso, dibuja la pantalla: título, tarjetas, gráfico, tabla y lugar de los filtros. Escribe qué pregunta responde cada elemento. No hace falta dibujar bien: ese boceto permite comprobar si la IA respetó tu intención.

Luego agrega tres ejemplos propios:

1. **Un caso normal:** qué datos doy y qué resultado espero.
2. **Un caso incorrecto:** qué error debe detectar y cómo me debe ayudar.
3. **Un cambio de interacción:** qué debe pasar cuando aplico un filtro o cambio el archivo.

El docente puede sugerir empezar por los límites, pero el alumno debe completar las ocho respuestas. No pasar a la IA sin una forma concreta de comprobar al menos el primer resultado.

## 3. Mi tabla para decidir si la IA cumplió

Antes de pedir cada hito, escribe la expectativa. Después de ejecutarlo, completa lo observado. No rellenes la evidencia con una respuesta del chat: usa lo que ocurrió al abrir el programa o ejecutar una prueba.

| ID | Lo que pido en papel | Qué espero observar | Cómo lo compruebo |
|---|---|---|---|
| C01 | Mostrar cinco ejemplos preparados | Dos positivos, dos negativos y uno neutral; 40%, 40% y 20% | Cuento las cinco filas y calculo las proporciones. |
| C02 | Cargar un CSV válido | Aparecen las filas aceptadas y se informa cualquier descarte | Comparo el archivo con la vista previa. |
| C03 | Detectar un CSV sin texto | Mensaje comprensible que indica la columna necesaria | Cargo a propósito un archivo sin esa columna. |
| C04 | Clasificar por reglas | Una etiqueta por comentario y método identificado | Reviso las palabras de ejemplo y la regla acordada. |
| C05 | Analizar diez de veinte comentarios | Exactamente diez resultados unidos a los ids correctos | Cuento e identifico las filas analizadas. |
| C06 | Filtrar negativos | Los datos de la tabla y los indicadores corresponden al filtro | Comparo sus ids y cantidades. |
| C07 | Descargar lo que estoy viendo | El CSV contiene las mismas filas visibles | Abro la descarga y comparo los ids. |
| C08 | Conservar un análisis mientras filtro | Cambiar el filtro no borra resultados ni repite la clasificación | Cambio dos veces de filtro y reviso los resultados y el registro o contador de ejecuciones. |
| C09 | Cambiar el archivo de entrada | No aparecen resultados del archivo anterior como si fueran del nuevo | Cargo otro CSV con ids distintos. |
| C10 | No ocultar errores | Un fallo queda como error; no aumenta Neutral | Provoco un fallo controlado mediante una prueba y reviso su estado. |
| C11 | Presentar fechas reales | La tendencia ordena y agrupa fechas válidas; no aparece si faltan | Uso fechas desordenadas y después un CSV sin fechas. |
| C12 | Hacer una mejora propia | Ocurre el cambio definido por mí sin romper lo anterior | Escribo y ejecuto un ejemplo antes/después. |

C01 comprueba una pantalla inicial con etiquetas preparadas, no el rendimiento de un clasificador. Al introducir reglas en C04, se sustituyen esas etiquetas y se vuelve a comprobar el resultado según las reglas acordadas. La prueba manual de proporciones puede usar una tabla de prueba separada con categorías conocidas.

No hace falta resolver todos los criterios a la vez. Para cada hito, usar los que correspondan. Si no se llega a una función durante la sesión, se marca pendiente y se retoma después.

Plantilla para completar a mano, una fila por criterio:

| ID | Esperaba | Observé realmente | Evidencia | Mi decisión |
|---|---|---|---|---|
| ___ | ___ | ___ | Cuenta, archivo, captura o salida de prueba: ___ | Cumple / No cumple / Pendiente |

**La decisión la toma el alumno.** Una prueba automática puede aportar evidencia; que la IA diga «terminado» no completa esta tabla.

## 4. Dos formas de trabajar con IA

### Ruta principal: OpenCode

El docente prepara una versión y un modelo con acceso comprobado. El alumno abre su carpeta nueva y entrega la hoja de papel y el prompt del hito. El agente puede crear archivos y ejecutar comandos; el alumno abre el panel, revisa la evidencia y decide si cumplió.

En la carpeta del proyecto, AGENTS.md conserva las reglas de trabajo. El complemento incluye un contenido propuesto. Tener ese archivo no reemplaza escribir una petición concreta ni comprobar el resultado.

### Alternativa: Qwen o DeepSeek en el navegador

Usa el adaptador de chat del complemento. Pide archivos completos, separados por nombre y en tandas pequeñas. Copia cada archivo en la ubicación indicada, guarda, ejecuta el comando y revisa el resultado. Si el chat no tiene acceso al equipo, no puede afirmar que ejecutó o comprobó el programa.

No se exige una API para esta ruta. El acceso al chat se ensaya antes de clase: puede requerir cuenta y tener límites. Si un alumno no puede acceder, trabaja por parejas alternando quién dirige y quién opera; cada uno completa su propia hoja y comprobación. Si falla el servicio, el docente usa un punto de recuperación preparado y registra qué parte queda pendiente de generar con IA.

La evaluación es la misma en ambas rutas. Copiar código no es una falta: copiar sin comprobarlo deja incompleto el trabajo.

## 5. Los datos y la lógica que debemos entender

Para la práctica usamos comentarios inventados, sin nombres ni cuentas reales. No descargamos datos de redes sociales como requisito inicial.

| Columna | Significado | Regla de la clase |
|---|---|---|
| texto | Comentario que se va a analizar | Obligatoria; las filas vacías se rechazan informando cuántas. |
| comment_id | Identificador del comentario | Único; si falta se genera para esa carga. No identifica personas. |
| fecha | Momento del comentario | Opcional; se valida y convierte antes de una gráfica temporal. |
| likes | Reacciones al comentario | Opcional; no mide si el comentario es positivo o negativo. |

Ejemplo:

```csv
comment_id,texto,fecha,likes
c01,"Excelente receta, gracias",2026-10-01,7
c02,"El sonido es horrible",2026-10-02,2
c03,"El video dura diez minutos",2026-10-02,1
```

El alumno debe poder contar el recorrido: **leo -> valido -> limpio informando cambios -> selecciono el lote -> clasifico -> guardo resultados de esa entrada -> filtro -> muestro y descargo**.

La clasificación inicial cuenta palabras de listas positivas y negativas, según reglas acordadas de normalización y empate. Sirve para entender condiciones y repeticiones. Puede fallar con negación, sarcasmo y contexto. Un error de procesamiento tiene un estado distinto de Neutral.

No se atribuye al texto la capacidad de revelar cómo se siente realmente una persona. Si más adelante se usan datos reales, habrá una actividad específica para decidir qué puede utilizarse y qué debe eliminarse; cambiar un nombre por un hash no elimina los posibles identificadores del texto.

## 6. Cómo ordenar el proyecto sin perder el primer logro

Primero construimos una pantalla pequeña que ya podemos ver. Después extraemos sus funciones para probarlas mejor. Así la estructura responde a una necesidad que el alumno ya experimentó.

Estructura de destino de la carpeta nueva, compartida con el complemento:

```text
vibe-check/
  AGENTS.md
  README.md
  requirements.txt
  .gitignore
  docs/
    00-hoja-de-papel.md
    diccionario-de-datos.md
    decisiones.md
    verificacion.md
  data/sample/comentarios.csv
  src/analizador/
    __init__.py
    io.py
    metricas.py
    sentimiento.py
  app/main.py
  tests/
```

`io.py` recibe y valida datos; `metricas.py` calcula cantidades; `sentimiento.py` clasifica; `app/main.py` organiza la interacción y presenta. Las funciones que calculan se prueban sin abrir el navegador. El primer hito todavía puede usar un único archivo provisional.

Los ejemplos se incluyen para que la app arranque sin archivos privados. El entorno virtual, cachés, secretos y datos reales quedan fuera del repositorio. La IA debe hacer funcionar los imports desde la raíz y registrar las dependencias verificadas. No se pide al alumno resolver rutas internas ni instalaciones de paquetes a ciegas.

## 7. Plan de dos horas y relación con los prompts

La preparación de equipos ocurre antes: Python, editor, dependencias, acceso a OpenCode o chat y comandos ensayados. Los tiempos son una propuesta para pilotear; el primer panel en media hora requiere esa preparación.

| Minutos | Trabajo | Prompt del complemento | Papel y evidencia |
|---|---|---|---|
| 0–5 | Ver el panel de ejemplo y elegir un tema | Sin prompt | Reconocer el usuario y la utilidad. |
| 5–15 | Completar las ocho preguntas y el boceto | Sin IA | Hoja y primer caso esperado. |
| 15–20 | Revisar la hoja con la IA y elegir plan | Hito 0 | Corregir el plan si no respeta el papel. |
| 20–30 | Crear el primer panel | Hito 1 | C01: contar filas y porcentajes. |
| 30–45 | Cargar y validar archivos | Hito 2 | C02 y C03: un CSV correcto y uno incorrecto. |
| 45–60 | Incorporar reglas y límite de lote | Hito 3 | C04, C05, C08 y C09. |
| 60–75 | Filtros, descarga y fechas | Hito 4 | C06, C07 y C11. |
| 75–95 | Ejecutar pruebas y evaluar casos nuevos | Hito 5 | C10 y revisión de criterios anteriores. |
| 95–110 | Mejora personal y revisión por parejas | Hito 6 | C12, propuesta antes de código. |
| 110–120 | Comparar el producto con el papel | Cierre | Cumple, no cumple o pendiente por criterio. |

Si falta tiempo, reducir funciones y mantener la comprobación y el cierre. Git, Ruff, el modelo real y la publicación pueden desarrollarse en otra sesión. Un punto de retorno puede empezar como una copia del hito y pasar después a un commit local.

## 8. El ciclo que repetimos en cada hito

```text
PAPEL      -> Escribo qué debe hacer y un ejemplo del resultado.
PLAN       -> La IA propone hasta tres pasos.
REVISIÓN   -> Yo comparo el plan con mi papel y lo corrijo.
CÓDIGO     -> Pido implementar solo ese hito.
EJECUCIÓN  -> Abro el programa y ejecuto las pruebas pertinentes.
COMPARACIÓN-> Registro esperado, observado y evidencia.
DECISIÓN   -> Yo marco cumple, no cumple o pendiente.
GUARDADO   -> Conservo el resultado que funciona y paso al siguiente hito.
```

No cambiar el papel después de ver el resultado solo para declarar que la IA cumplió. Si cambia una necesidad, registrar por qué, actualizar el criterio y comprobarlo otra vez. Si el criterio estaba mal, corregirlo con una explicación; no conservar una expectativa equivocada por obligación.

### Prompt común: convertir mi papel en un paso

```text
Este es el criterio [ID] que escribí antes de pedir código:
Quiero: [comportamiento].
Entrada de ejemplo: [datos].
Resultado esperado: [resultado que yo calculé o describí].
Lo comprobaré así: [acción o prueba].
No debes cambiar: [límite de alcance].

Resume lo que entendiste y propón hasta tres pasos. Señala contradicciones. No implementes todavía. Espera mi revisión y luego trabaja solo en el hito acordado. No des por cumplido mi criterio: yo revisaré el resultado real.
```

### Prompt común: revisar lo que hizo la IA

```text
Para el criterio [ID], esperaba [resultado], pero al ejecutar observé [resultado real]. Esta es mi evidencia: [salida, cuenta manual o pasos].
Compara ambos sin asumir que tu código es correcto. Explica si el problema está en la implementación, los datos o la expectativa y cómo lo confirmarías. Propón la corrección mínima. No cambies un criterio correcto para hacer pasar el programa. Después de corregir, dame la forma de repetir la comprobación. Yo completaré la decisión en mi hoja.
```

### Prompt común: entender una función

```text
Explícame esta función usando un comentario de ejemplo. Dime qué entra, qué decide o repite y qué sale. Luego explica las líneas necesarias para entender ese recorrido. Señala cualquier supuesto que no estuviera en mi hoja. Hazme una pregunta breve y espera mi respuesta.
```

Los prompts completos de construcción están en el complemento. Antes de cada uno, incluir el criterio del papel correspondiente; después, completar la tabla de verificación. Si se usa chat, pegar también el adaptador y los archivos relevantes.

## 9. Probar el programa y evaluar el clasificador

Hay tres comprobaciones diferentes:

| Comprobación | Pregunta | Ejemplo |
|---|---|---|
| Del programa | ¿Cumple la acción que pedí? | El CSV sin texto recibe ayuda y no rompe la pantalla. |
| De la clasificación | ¿La etiqueta resulta razonable frente a una referencia humana? | Mi etiqueta de un comentario nuevo discrepa de la regla. |
| Del uso | ¿Otra persona entiende cómo resolver su tarea? | Un compañero filtra negativos y descarga lo que ve. |

Una prueba que pasa no demuestra que el clasificador entiende el sarcasmo. Una interfaz agradable tampoco demuestra que cuenta bien.

Para evaluar en clase, cada alumno etiqueta cinco comentarios nuevos **antes** de ver la predicción. Marca los ambiguos, compara y explica un desacuerdo. La tarea posterior amplía a 50 casos y documenta cómo se eligieron. Las etiquetas de referencia se mantienen separadas de la entrada del clasificador.

El porcentaje de acuerdo se reporta con el número de casos evaluados y los errores por separado. No se presenta como rendimiento universal ni como margen de error de los porcentajes del panel. Si se incorpora un modelo, se verifica su evaluación concreta antes de citar cifras; F1 y porcentaje de acierto son medidas distintas.

Para ejecutar desde la raíz de la carpeta educativa en Windows:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app/main.py
```

Las pruebas, en otra terminal:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Estos son los comandos de destino para la app que construirán los alumnos. El repositorio actual conserva su comando con `app.py`. Si el entorno usa otra ruta, el docente adapta y comprueba los comandos antes de imprimirlos.

## 10. Errores que debemos aprender a descubrir

| Error | Qué puede parecer | Cómo lo detecta el alumno |
|---|---|---|
| El programa analiza diez filas y guarda en veinte | «Terminó el análisis» | C05: contar resultados y revisar ids. |
| Un fallo se convierte en Neutral | «Todos se pudieron clasificar» | C10: provocar un fallo controlado y revisar estados. |
| El gráfico usa datos diferentes de la tabla | «El panel se ve completo» | C06 y C07: comparar cantidades e ids. |
| El filtro borra el análisis | «Solo cambió una opción» | C08: repetir la interacción y observar. |
| Se conserva el resultado de otro archivo | «Los datos siguen cargados» | C09: subir otro archivo con ids distintos. |
| La posición de una fila se muestra como tiempo | «Hay una tendencia» | C11: comprobar la fecha usada y el orden. |
| La IA afirma que ejecutó sin tener herramientas | «Las pruebas pasaron» | Pedir el comando y revisar su salida real en el equipo. |
| El chat entrega un fragmento incompleto | «Solo falta pegarlo» | Pedir archivo completo y ruta; ejecutar antes del siguiente cambio. |

No hace falta que el alumno diagnostique solo la causa técnica. Su responsabilidad inicial es reconocer la diferencia entre esperado y observado, reproducirla y pedir ayuda precisa.

## 11. Checklist de la sesión

Antes:

- [ ] Escribí las ocho respuestas, un boceto y un resultado esperado.
- [ ] Entiendo qué datos son de ejemplo y qué funciones quedan fuera.
- [ ] Puedo acceder a la ruta de IA elegida o tengo una alternativa acordada.

Durante cada hito:

- [ ] El plan corresponde a mi papel.
- [ ] Pedí un cambio limitado y entiendo su entrada, proceso y salida.
- [ ] Ejecuté el programa y las pruebas pertinentes, o registré por qué quedaron pendientes.
- [ ] Comparé esperado y observado; conservé evidencia real.
- [ ] Guardé el punto que funciona y anoté el fallo que corregí.

Después:

- [ ] Revisé cada criterio y marqué cumple, no cumple o pendiente.
- [ ] Un compañero probó la app con una pregunta del usuario.
- [ ] Los límites del método son visibles y los ejemplos no contienen datos personales.
- [ ] El README permite repetir los pasos y mi registro conserva decisiones.
- [ ] Puedo explicar una decisión, una prueba y una mejora propia.

## 12. Entrega y evaluación

Entregar la hoja de papel original, la carpeta de la app, el registro de verificación y una demostración de dos minutos. Al digitalizar, guardar la transcripción de las expectativas en `docs/00-hoja-de-papel.md` y los resultados en `docs/verificacion.md`. Una foto del papel puede acompañar la entrega, pero no es obligatorio subirla a un repositorio público.

| Aspecto | Puntos | Evidencia |
|---|---:|---|
| Problema y expectativas anteriores al código | 25 | Hoja y ejemplos propios. |
| Comprobación de si la IA cumplió | 35 | Tabla con esperado, observado, evidencia y decisión del alumno. |
| Comprensión del flujo y de un cambio | 20 | Explicación con un comentario y mejora justificada. |
| Presentación y uso | 10 | Panel legible que otra persona puede usar. |
| Límites y registro | 10 | Distingue reglas/modelo, error/neutral y comprobado/pendiente. |

La estética motiva y se evalúa; el mayor peso está en pensar y verificar. No se evalúa por cantidad de código ni por tener una suscripción. La entrega local no requiere publicar; la publicación será un hito posterior con acceso a las cuentas necesarias.

## 13. Tarea y continuidad

1. Completar un criterio pendiente o proponer uno nuevo por escrito antes de pedir código.
2. Realizar la comparación humana con 50 comentarios nuevos y explicar dos desacuerdos.
3. Pedir a otra persona que ejecute el proyecto siguiendo el README y registrar dónde necesitó ayuda.
4. En la siguiente sesión, preparar GitHub y publicación, o comparar reglas con un modelo real. Escribir primero qué comportamiento esperamos conservar y cómo verificaremos que se conserva.

Para el docente: ensayar el guion con una persona principiante, comprobar instalación y acceso antes de clase y preparar puntos de recuperación. El objetivo del primer panel en 25–30 minutos es una meta a validar. Si el ritmo exige elegir, reducir alcance y conservar el papel y la verificación.

**La clase termina cuando el alumno puede mostrar qué pidió, qué hizo la IA y qué evidencia tiene para decidir si cumplió.**
