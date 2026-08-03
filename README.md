# 🎭 Vibe Check IA: Analizador de Sentimientos en Twitter

> Analiza el sentimiento de tweets en español usando Inteligencia Artificial (Google Gemini) y visualiza resultados en un dashboard interactivo.

---

## Descripción

**Vibe Check IA** es una aplicación web local que:

1. Lee un dataset de tweets en español clasificados por sentimiento.
2. Usa la API de **Google Gemini** (modelo `gemini-flash-latest`) para analizar el sentimiento de cada tweet.
3. Muestra gráficos interactivos (pastel, barras y línea de tiempo) en un dashboard con **Streamlit**.
4. Permite filtrar tweets por tipo de sentimiento (Positivo, Negativo, Neutral, etc.).

---

## Dataset

Este proyecto utiliza el dataset público de Kaggle:

**[Twitter Sentiment Analysis in Spanish Tweets](https://www.kaggle.com/datasets/philipsanm/sentiment-analysis-in-spanish-tweets)** de PhilipSanM

### ¿Cómo descargar el dataset?

1. Ve a la página del dataset en Kaggle:  
   👉 https://www.kaggle.com/datasets/philipsanm/sentiment-analysis-in-spanish-tweets
2. Haz clic en el botón **"Download"**.
3. Descomprime el archivo ZIP.
4. Busca el archivo CSV (generalmente se llama `tweets.csv` o similar).
5. Renómbralo a **`tweets_espanol.csv`**.
6. Colócalo dentro de la carpeta `data/` de este proyecto.

### Estructura esperada del CSV

El dataset debe tener al menos estas columnas:

| Columna | Descripción |
|---------|-------------|
| `tweet` | El texto del tweet en español |
| `sentimiento` | Sentimiento del tweet (Positivo, Negativo, Neutral, etc.) |

> **Nota:** El archivo `data/tweets_espanol.csv` NO se sube a GitHub por ser un archivo grande. Cada desarrollador debe descargarlo por separado.

---

## Requisitos previos

- **Python 3.10** o superior
- **VS Code** con la extensión de Python
- **API Key de Google Gemini** (ver instrucciones abajo)
- **Git** (opcional, para versionar)

---

## Instalación paso a paso

### 1. Clonar o descargar el proyecto

```bash
git clone https://github.com/TU_USUARIO/Vibe_Check_IA.git
cd Vibe_Check_IA
```

O descarga el ZIP desde GitHub y descomprímelo.

### 2. Crear entorno virtual

En la terminal de VS Code:

```bash
python -m venv venv
```

Actívalo:

**Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la API Key de Google Gemini

1. Ve a [Google AI Studio](https://aistudio.google.com/apikey).
2. Crea una cuenta o inicia sesión.
3. Haz clic en **"Create API Key"**.
4. Copia la clave generada.
5. Abre el archivo `.env` en la raíz del proyecto.
6. Reemplaza el contenido con tu clave:

```
GOOGLE_API_KEY=tu_clave_de_api_aqui
```

> ⚠️ **NUNCA** subas tu `.env` a GitHub. El archivo `.gitignore` ya lo excluye.

### 5. Descargar el dataset

Sigue las instrucciones de la sección **"Dataset"** más arriba y coloca el archivo en `data/tweets_espanol.csv`.

### 6. Ejecutar los tests (opcional)

```bash
pytest tests/ --cov=src --cov-report=term-missing --cov-fail-under=90
```

### 7. Lanzar el dashboard

```bash
streamlit run app.py
```

Se abrirá automáticamente en tu navegador en: **http://localhost:8501**

---

## Estructura del proyecto

```
Vibe_Check_IA/
├── .env                          # API Key secreta de Google Gemini
├── .gitignore                    # Archivos que NO se suben a GitHub
├── requirements.txt              # Librerías necesarias
├── context.md                    # Contexto del proyecto
├── arquitectura.md               # Arquitectura (estándar arc42)
├── estado.md                     # Estado y roadmap del proyecto
├── README.md                     # Este archivo
├── src/
│   ├── __init__.py               # Hace que src/ sea un paquete Python
│   ├── analizador.py             # Lógica de análisis con Gemini
│   ├── datos.py                  # Lectura y limpieza del CSV
│   └── graficos.py               # Generación de gráficos con Plotly
├── app.py                        # Dashboard principal con Streamlit
├── tests/
│   ├── __init__.py               # Hace que tests/ sea un paquete Python
│   ├── test_analizador.py        # Tests del analizador
│   ├── test_datos.py             # Tests de datos
│   └── test_graficos.py          # Tests de gráficos
└── data/
    └── tweets_espanol.csv        # Dataset de Kaggle (NO se sube)
```

---

## Cómo funciona

```
1. Abres http://localhost:8501 en tu navegador
2. El dashboard carga el dataset de tweets
3. Seleccionas un filtro de sentimiento en el sidebar
4. Presionas el botón "Analizar Tweets"
5. Google Gemini analiza cada tweet y confirma el sentimiento
6. Se muestran 3 gráficos interactivos:
   - 🥧 Pastel: distribución de sentimientos
   - 📊 Barras: conteo de emociones
   - 📈 Línea de tiempo: evolución temporal
7. Puedes explorar los datos en una tabla interactiva
```

---

## Comandos útiles

| Comando | Descripción |
|---------|-------------|
| `streamlit run app.py` | Lanzar el dashboard |
| `pytest tests/` | Ejecutar todos los tests |
| `pytest tests/ --cov=src` | Tests con cobertura de código |
| `pip install -r requirements.txt` | Instalar dependencias |

---

## Tecnologías usadas

| Tecnología | Para qué |
|------------|----------|
| Python 3.10+ | Lenguaje de programación |
| Streamlit | Dashboard web interactivo |
| Google Gemini (gemini-flash-latest) | Análisis de sentimientos con IA |
| Plotly | Gráficos interactivos |
| Pandas | Lectura y manipulación de datos |
| pytest | Tests automatizados |
| python-dotenv | Variables de entorno seguras |

---

## Licencia

Este proyecto es educativo. Puedes usarlo libremente para aprender.

---

## Créditos

- **Dataset:** [Twitter Sentiment Analysis in Spanish Tweets](https://www.kaggle.com/datasets/philipsanm/sentiment-analysis-in-spanish-tweets) por PhilipSanM en Kaggle.
- **API de IA:** Google Gemini por Google AI.
- **Dashboard:** Streamlit por Streamlit Inc.
