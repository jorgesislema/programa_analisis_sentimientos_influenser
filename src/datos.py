"""
(datos.py) Este archivo se encarga de LEER y LIMPIAR los datos de los tweets.

¿Qué hace?
- Abre el archivo CSV (como si fuera una tabla de Excel guardada como texto).
- Lo convierte en un "DataFrame" (una tabla que Python puede manipular).
- Limpia datos basura (tweets vacíos, espacios de más, etc.).
- Filtra tweets por tipo de sentimiento cuando el usuario lo pide.

¿Qué es un CSV?
Un CSV (Comma-Separated Values) es un archivo de texto donde los datos
están separados por comas. Es como una tabla donde cada fila es una línea
y cada columna está separada por una coma. Ejemplo:
    tweet,sentimiento
    "Hoy hace sol",Positivo
    "Estoy triste",Negativo
"""

# ============================================================
# IMPORTACIONES
# ============================================================
# "import" es como traer una caja de herramientas a tu proyecto.
# Cada import trae una herramienta diferente.

import os
import pandas as pd


# Traducción de sentimientos del dataset (inglés → español)
TRADUCCION_SENTIMIENTOS = {
    "scared": "Asustado",
    "mad": "Enojado",
    "sad": "Triste",
    "peaceful": "Tranquilo",
    "powerful": "Poderoso",
    "joyful": "Alegre",
}

# Traducción de emociones del dataset (inglés → español)
TRADUCCION_EMOCIONES = {
    "overwhelmed": "Abrumado",
    "embarrassed": "Avergonzado",
    "jealous": "Celoso",
    "irritated": "Irritado",
    "frustrated": "Frustrado",
    "distant": "Distante",
    "stupid": "Estúpido",
    "isolated": "Aislado",
    "sleepy": "Somnoliento",
    "responsive": "Receptivo",
    "relaxed": "Relajado",
    "loving": "Amoroso",
    "thankful": "Agradecido",
    "secure": "Seguro",
    "confident": "Seguro de sí",
    "successful": "Exitoso",
    "surprised": "Sorprendido",
    "playful": "Juguetón",
    "optimistic": "Optimista",
    "daring": "Atrevido",
}


# ============================================================
# FUNCIONES
# ============================================================

def leer_csv(ruta_csv: str) -> pd.DataFrame:
    """
    Lee un archivo CSV y lo convierte en un DataFrame.

    ¿Qué es un DataFrame?
    Imagina una tabla de Excel. Un DataFrame es EXACTAMENTE eso,
    pero dentro de Python. Tiene filas, columnas, y puedes hacer
    cosas como filtrar, ordenar, y contar.

    Parámetros:
        ruta_csv (str): La ruta del archivo CSV. Ejemplo: "data/tweets.csv"

    Retorna:
        pd.DataFrame: Una tabla con los datos del CSV.

    Ejemplo de uso:
        df = leer_csv("data/tweets.csv")
        print(df.head())  # Muestra las primeras 5 filas
    """
    # Verificamos que el archivo exista antes de intentar leerlo.
    # Esto es como preguntar: "¿Está el libro en la biblioteca?"
    # antes de intentar abrirlo.
    if not os.path.exists(ruta_csv):
        # Si no existe, lanzamos un error claro para que sepamos qué pasó.
        raise FileNotFoundError(
            f"No encontré el archivo CSV en: {ruta_csv}\n"
            "Por favor, descarga el dataset de Kaggle y colócalo en la carpeta data/."
        )

    # pd.read_csv() es la función mágica de Pandas que:
    # 1. Abre el archivo CSV
    # 2. Lee cada línea
    # 3. Separa los datos por comas
    # 4. Crea un DataFrame (tabla) con todo organizado
    df = pd.read_csv(ruta_csv)

    # Renombramos columnas para que coincidan con lo que espera el resto del código
    columnas_renombre = {
        "text": "tweet",
        "sentiment": "sentimiento",
        "emotion": "emocion",
    }
    df = df.rename(columns={k: v for k, v in columnas_renombre.items() if k in df.columns})

    print(f"CSV cargado correctamente: {len(df)} filas, {len(df.columns)} columnas")

    return df


def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el DataFrame eliminando basura: tweets vacíos, espacios extra, etc.

    ¿Por qué limpiar?
    Porque los datos del mundo real son "sucios". A veces hay:
    - Tweets vacíos (sin texto)
    - Espacios de más al inicio o final
    - Valores que no tienen sentido

    Parámetros:
        df (pd.DataFrame): El DataFrame original (sucio).

    Retorna:
        pd.DataFrame: Un DataFrame limpio, sin basura.
    """
    # Hacemos una COPIA del DataFrame original.
    # ¿Por qué una copia? Porque no queremos destruir los datos originales.
    # Es como fotocopiar un documento antes de escribir en él.
    df_limpio = df.copy()

    # ---- PASO 1: Eliminar filas donde el tweet esté vacío ----
    # Si la columna "tweet" está vacía (NaN), esa fila no sirve.
    # .dropna(subset=["tweet"]) elimina esas filas vacías.
    df_limpio = df_limpio.dropna(subset=["tweet"])

    # ---- PASO 2: Eliminar tweets que son solo espacios en blanco ----
    # .str.strip() quita espacios al inicio y final de cada tweet.
    # Luego filtramos para quedarnos solo con tweets que tengan texto real.
    df_limpio["tweet"] = df_limpio["tweet"].str.strip()
    df_limpio = df_limpio[df_limpio["tweet"] != ""]

    # ---- PASO 3: Resetear los índices ----
    # Cuando eliminas filas, los números de las filas quedan desordenados.
    # .reset_index(drop=True) los reorganiza desde 0, 1, 2, 3...
    df_limpio = df_limpio.reset_index(drop=True)

    # Traducir sentimientos y emociones del inglés al español
    if "sentimiento" in df_limpio.columns:
        df_limpio["sentimiento"] = df_limpio["sentimiento"].map(
            lambda x: TRADUCCION_SENTIMIENTOS.get(x, x) if pd.notna(x) else x
        )
    if "emocion" in df_limpio.columns:
        df_limpio["emocion"] = df_limpio["emocion"].map(
            lambda x: TRADUCCION_EMOCIONES.get(x, x) if pd.notna(x) else x
        )

    print(f"Datos limpiados: quedan {len(df_limpio)} filas válidas")
    return df_limpio


def filtrar_por_sentimiento(df: pd.DataFrame, sentimiento: str) -> pd.DataFrame:
    """
    Filtra el DataFrame para mostrar solo los tweets de un sentimiento específico.

    ¿Qué es filtrar?
    Es como tener una caja de 100 pelotas de diferentes colores y
    sacar solo las rojas. Filtrar es separar lo que te interesa de lo demás.

    Parámetros:
        df (pd.DataFrame): El DataFrame completo.
        sentimiento (str): El sentimiento a filtrar. Ejemplo: "Positivo"

    Retorna:
        pd.DataFrame: Solo los tweets con ese sentimiento.
    """
    # Si el usuario no eligió ningún sentimiento ("Todos"), devolvemos todo.
    if sentimiento == "Todos":
        return df

    # .str.lower() convierte todo a minúsculas para que la comparación funcione.
    # .str.contains() busca si el texto contiene la palabra del sentimiento.
    # Esto hace que "Positivo", "positivo", "POSITIVO" funcionen igual.
    mascara = df["sentimiento"].str.lower().str.contains(sentimiento.lower(), na=False)

    # El DataFrame filtrado solo contiene las filas donde mascara es True.
    df_filtrado = df[mascara].copy()
    df_filtrado = df_filtrado.reset_index(drop=True)

    print(f"Filtro '{sentimiento}': {len(df_filtrado)} tweets encontrados")
    return df_filtrado


def obtener_sentimientos_unicos(df: pd.DataFrame) -> list:
    """
    Obtiene la lista de todos los sentimientos únicos que existen en el DataFrame.

    ¿Para qué sirve?
    Para saber qué opciones de filtro ofrecer al usuario.
    Si en el CSV hay "Positivo", "Negativo" y "Neutral",
    esta función devuelve esa lista para que Streamlit la muestre.

    Parámetros:
        df (pd.DataFrame): El DataFrame con los tweets.

    Retorna:
        list: Una lista con los sentimientos únicos. Ejemplo: ["Positivo", "Negativo", "Neutral"]
    """
    # .unique() devuelve los valores que se repiten (sin duplicados).
    # .tolist() convierte ese array de NumPy en una lista normal de Python.
    sentimientos = df["sentimiento"].unique().tolist()

    # Agregamos "Todos" al inicio para que el usuario pueda ver todos los tweets.
    sentimientos.insert(0, "Todos")

    return sentimientos
