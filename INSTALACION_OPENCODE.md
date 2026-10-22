# Instalar Node.js y OpenCode sin contraseña de administrador

Guía para Windows 10/11 usando la terminal de VS Code. No necesitas ser administrador ni conocer la contraseña del equipo.

Si un instalador muestra una ventana de **Control de cuentas de usuario (UAC)** pidiendo la contraseña del administrador, cancela: ese método no es el de esta guía. Los pasos de abajo instalan todo dentro de tu carpeta de usuario.

## 0. Antes de empezar

- Ten VS Code abierto. Si no está instalado, pídelo al docente: instalarlo puede requerir permisos.
- Abre la terminal con **Terminal > Nueva terminal**. El atajo es `Ctrl` más la tecla de acento grave, debajo de `Esc` (en teclado español suele ser `Ctrl + ñ`).
- Comprueba que la terminal es **PowerShell** (lo indica arriba a la derecha).
- Necesitas internet.
- No compartas contraseñas ni claves de API. Si el docente entrega un acceso, úsalo solo en tu equipo.

Comprueba que PowerShell responde:

```powershell
$PSVersionTable.PSVersion
```

## 1. Descargar Node.js sin instalador

Node.js es el programa que necesita OpenCode para ejecutarse. El instalador `.msi` pide permisos de administrador; el ZIP no.

Copia y ejecuta **un bloque por vez** en PowerShell:

```powershell
# Versión LTS de ejemplo. Comprueba el número actual en https://nodejs.org/en/download
$version = "v24.22.1"

# Descargar el ZIP oficial a la carpeta temporal
$zip = Join-Path $env:TEMP "node-$version-win-x64.zip"
Invoke-WebRequest "https://nodejs.org/dist/$version/node-$version-win-x64.zip" -OutFile $zip
```

```powershell
# Extraer dentro de tu perfil de usuario
$dest = Join-Path $env:LOCALAPPDATA "Programs\nodejs"
New-Item -ItemType Directory -Force -Path $dest | Out-Null
Expand-Archive -Path $zip -DestinationPath $dest -Force
Move-Item -Path (Join-Path $dest "node-$version-win-x64\*") -Destination $dest -Force
Remove-Item -Path (Join-Path $dest "node-$version-win-x64") -Recurse -Force
```

```powershell
# Agregar Node.js al PATH del usuario (sin administrador)
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($userPath -notlike "*$dest*") {
    [Environment]::SetEnvironmentVariable("Path", "$dest;$userPath", "User")
}
$env:Path = "$dest;$env:Path"
```

```powershell
# Comprobar
node --version
npm --version
```

Debes ver dos números de versión. Si `node` no se reconoce, cierra VS Code, ábrelo otra vez y repite la comprobación. Si aparece una versión distinta, ya había otro Node instalado: ejecuta `where node` para ver cuál se está usando. Cualquier versión moderna sirve para OpenCode.

### Si no quieres usar la terminal para descargar

1. Entra en [nodejs.org/en/download](https://nodejs.org/en/download).
2. Descarga el **ZIP para Windows x64** de la versión LTS.
3. Extrae el contenido en `C:\Users\TU_USUARIO\AppData\Local\Programs\nodejs`.
4. Agrega esa carpeta al `Path` de tu usuario y reabre VS Code.

No descargues Node.js de sitios que no sean `nodejs.org`.

## 2. Instalar OpenCode con npm

`npm` viene con Node.js. Configura una carpeta de instalación dentro de tu usuario para no necesitar permisos:

```powershell
$npmPrefix = Join-Path $env:LOCALAPPDATA "npm"
New-Item -ItemType Directory -Force -Path $npmPrefix | Out-Null
npm config set prefix "$npmPrefix"
```

```powershell
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($userPath -notlike "*$npmPrefix*") {
    [Environment]::SetEnvironmentVariable("Path", "$npmPrefix;$userPath", "User")
}
$env:Path = "$npmPrefix;$env:Path"
```

```powershell
npm install -g opencode-ai
opencode --version
```

Si `opencode` no se reconoce, cierra VS Code, ábrelo de nuevo y prueba otra vez.

Si `npm install -g opencode-ai` falla por red o permisos, descarga el binario para Windows x64 desde [las releases oficiales](https://github.com/anomalyco/opencode/releases), guárdalo en una carpeta de tu usuario y agrega esa carpeta al `Path` como hiciste con Node.js.

> La documentación oficial también ofrece Chocolatey, Scoop, WSL y binarios. Esta guía usa npm porque funciona en la carpeta del usuario y no exige administrador. No mezcles instrucciones de OpenCode 1 y OpenCode 2.

## 3. Abrir OpenCode en tu proyecto

```powershell
cd "C:\ruta\a\tu\carpeta\vibe-check"
opencode
```

Dentro de OpenCode:

| Acción | Cómo |
|---|---|
| Configurar el proveedor de IA | `/connect` |
| Crear o revisar `AGENTS.md` | `/init` |
| Cambiar entre plan y construcción | `Tab` |
| Buscar y adjuntar un archivo | `@` |
| Deshacer el último cambio | `/undo` |
| Rehacer | `/redo` |
| Ayuda | `/help` |
| Salir | `Ctrl + C` |

La cuenta, la clave y el modelo los prepara el docente. La disponibilidad de modelos gratuitos cambia: no cuentes con que uno siga disponible siempre.

## 4. Código y prompts que usarás

Antes de pedir código, completa las [plantillas del alumno](plantillas/). El primer mensaje de OpenCode puede ser el de [la plantilla 1](plantillas/01-prompt-ingeniero.md). Resumido:

```text
Actúa como ingeniero de software con 40 años de experiencia. Tu trabajo es guiar a una persona que no programa para que entienda la lógica y construya su propio panel con Python y Streamlit.

Mi problema: ______________________________
Mi usuario: _______________________________
Datos de entrada: _________________________
Resultado que quiero: _____________________
Queda fuera: ______________________________
Lo comprobaré así: ________________________

Antes de escribir código, propón un plan de máximo tres pasos y espera mi revisión. Trabaja en un hito a la vez. Explica en español. No inventes pruebas ni resultados. No conviertas errores en Neutral. Al terminar, hazme una pregunta breve.
```

Después usa los hitos de [CLASE_OPENCODE_Y_CHAT.md](CLASE_OPENCODE_Y_CHAT.md) y las plantillas 2 a 5.

### Archivos que pedirás

```text
app/main.py
data/sample/comentarios.csv
src/analizador/__init__.py
src/analizador/io.py
src/analizador/metricas.py
src/analizador/sentimiento.py
tests/test_...py
docs/00-hoja-de-papel.md
docs/diccionario-de-datos.md
docs/decisiones.md
docs/verificacion.md
```

Pide un archivo por vez y compruébalo antes de seguir. No copies el código de la referencia sin entender qué recibe, qué procesa y qué devuelve.

### `AGENTS.md` para tu carpeta

Guarda este texto como `AGENTS.md` en la carpeta nueva. OpenCode lo lee al iniciar:

```markdown
# Proyecto de clase: Vibe Check
Somos principiantes. Explica en español y con pasos pequeños.
Stack: Python, Streamlit, Pandas, Plotly, pytest. Sin API ni modelo de IA.
Interfaz: app/main.py. Lógica: src/analizador/io.py, metricas.py, sentimiento.py.
Trabaja solo en el hito pedido. Antes, propón tres pasos y espera mi revisión.
Ejecuta las pruebas y reporta la salida real. Si no puedes, dilo.
No conviertas errores en Neutral ni inventes resultados. Solo datos sintéticos.
Al terminar, di qué debo observar y hazme una pregunta breve.
```

### Comandos que el agente puede ejecutar

Desde la carpeta del proyecto:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app/main.py
```

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Streamlit deja la terminal ocupada. Pide al agente que ejecute las pruebas y abre la app en otra terminal. Tú debes ver la salida real; no aceptes «las pruebas pasaron» sin evidencia.

## 5. Si algo falla

| Mensaje | Causa probable | Qué hacer |
|---|---|---|
| `node no se reconoce` | El PATH no se actualizó | Cierra y abre VS Code; revisa `$env:Path` |
| `node --version` muestra otra versión | Ya había Node instalado | Usa `where node`; no es un error si es moderna |
| `npm no se reconoce` | Node.js no está en el PATH | Repite el paso 1 y reabre la terminal |
| `opencode no se reconoce` | La carpeta `%LOCALAPPDATA%\npm` no está en el PATH | Repite el paso 2 y reabre VS Code |
| `EACCES` o permiso denegado | npm intenta escribir fuera de tu usuario | Revisa `npm config get prefix` |
| UAC pide contraseña | Usaste un instalador `.msi` o un método con administrador | Cancela y usa el ZIP de esta guía |
| Error de certificado o proxy | La red del aula bloquea la descarga | Avisa al docente; no desactives la seguridad |
| PowerShell bloquea un script | Política de ejecución | No cambies configuraciones sin ayuda; usa la ruta de chat |

No uses `sudo`, no desactives el antivirus y no ejecutes scripts de sitios desconocidos.

## 6. Comprobación final

Ejecuta en la terminal:

```powershell
node --version
npm --version
opencode --version
```

Y responde:

- ¿Qué versión de Node.js tienes?
- ¿Qué carpeta usó npm para instalar OpenCode?
- ¿Abrir `opencode` en tu carpeta muestra la interfaz?
- ¿Puedes explicar qué hace `/init` y para qué sirve `AGENTS.md`?
