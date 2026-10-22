# Estado de la referencia y del material de clase

Actualización documental: 22 de octubre de 2026.

## Qué puedes usar ahora

- Programa de referencia en app.py con CSV local, filtros y visualizaciones.
- Módulos de lectura y limpieza de datos, modelo local de pysentimiento y gráficos.
- [Clase para el alumno](../../Apuntes.md), [hoja de trabajo](../../HOJA_DE_TRABAJO.md) y [AGENTS.md en español](../../AGENTS.md).
- [Prompts por hitos](../../CLASE_OPENCODE_Y_CHAT.md) y [guía docente](clase_desarrollar_programa_con_ia.md).

El CSV local esperado está ignorado por Git. El docente debe prepararlo para mostrar el panel; no basta con descargar el repositorio para tener los datos.

## Comprobaciones efectuadas anteriormente

Se ejecutaron 15 pruebas de tests/test_datos.py y tests/test_graficos.py: todas pasaron, con cobertura conjunta de 92% para esos módulos. Se verificó la carga local de 2.590 filas y se reprodujo de forma aislada el error de asignar diez resultados a once filas.

Esto no confirma el rendimiento de pysentimiento, una instalación limpia, todos los recorridos de la interfaz ni un despliegue público. La documentación actualizada no se presenta como una nueva implementación de la app.

## Mejoras pendientes del código de referencia

- Corregir la asignación de un lote limitado a una tabla mayor en app.py.
- Separar error de procesamiento de Neutral; el analizador actual oculta excepciones devolviendo Neutral.
- Evitar equiparar automáticamente positivo con alegría y negativo con tristeza.
- Conservar resultados al interactuar y unificar los datos de indicadores, gráficos y tabla.
- Convertir y ordenar fechas antes de hablar de evolución temporal.
- Facilitar datos sintéticos incluidos y una ruta de instalación ligera.

Son casos útiles para practicar detección de problemas, pero no deben reproducirse como comportamiento correcto en la versión del alumno.

## Lo que se construirá durante la clase

En una carpeta nueva, con app/main.py: panel con ejemplos sintéticos, clasificación por reglas, validación, límite de lote, filtros, descarga, estados y pruebas. Su cumplimiento lo registra cada alumno con esperado, observado, evidencia y decisión.

El programa por reglas, la descarga y la estructura de esa reconstrucción se describen en los prompts; no se afirman implementados en app.py. La demostración real de esa nueva app requiere construirla y probarla.

## Continuaciones

Modelo real, evaluación con una muestra humana, GitHub y publicación. Se preparan por separado después del primer resultado local. Los tiempos del guion y el acceso a OpenCode o chats necesitan un ensayo en los equipos del aula.
