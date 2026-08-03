"""
(analizador.py) Este archivo se encarga de ANALIZAR el sentimiento de los tweets.

Usa pysentimiento, una librería de Python que tiene modelos de IA pre-entrenados
para analizar sentimientos en español. No necesita API key ni conexión a internet.

¿Qué es pysentimiento?
Es una caja de herramientas con "cerebros digitales" ya entrenados para entender
emociones en español, especialmente en tweets y redes sociales.
"""

from pysentimiento import create_analyzer
from pysentimiento.preprocessing import preprocess_tweet


# Mapeo de sentimientos del dataset a español con emojis
MAPEO_SENTIMIENTOS = {
    "scared": "😨 Asustado",
    "mad": "😡 Enojado",
    "sad": "😢 Triste",
    "peaceful": "😌 Tranquilo",
    "powerful": "💪 Poderoso",
    "joyful": "😄 Alegre",
}

# Sentimiento por defecto cuando pysentimiento detecta neutral
NEUTRAL = "😐 Neutral"


def obtener_analizador():
    """
    Crea y retorna el analizador de sentimientos de pysentimiento.
    Se llama una vez y se reutiliza para no cargar el modelo cada vez.
    """
    if not hasattr(obtener_analizador, "_analizador"):
        obtener_analizador._analizador = create_analyzer(task="sentiment", lang="es")
    return obtener_analizador._analizador


def clasificar_sentimiento(texto_tweet: str) -> str:
    """
    Analiza el sentimiento de un tweet usando pysentimiento.

    Parámetros:
        texto_tweet (str): El texto del tweet a analizar.

    Retorna:
        str: Una categoría de sentimiento en español con emoji.
    """
    try:
        analizador = obtener_analizador()
        tweet_limpio = preprocess_tweet(texto_tweet)
        resultado = analizador.predict(tweet_limpio)

        mapeo_pysentimiento = {
            "POS": "joyful",
            "NEG": "sad",
            "NEU": "neutral",
        }

        sentimiento_en = mapeo_pysentimiento.get(resultado.output, "neutral")

        return MAPEO_SENTIMIENTOS.get(sentimiento_en, NEUTRAL)

    except Exception as e:
        print(f"Error al analizar tweet: {e}")
        return NEUTRAL


def analizar_lote_tweets(tweets: list, max_tweets: int = 10) -> list:
    """
    Analiza varios tweets a la vez usando pysentimiento.

    Parámetros:
        tweets (list): Una lista de textos de tweets.
        max_tweets (int): Cuántos tweets analizar como máximo.

    Retorna:
        list: Una lista de sentimientos correspondientes a cada tweet.
    """
    sentimientos = []

    for i, tweet in enumerate(tweets[:max_tweets]):
        sentimiento = clasificar_sentimiento(tweet)
        sentimientos.append(sentimiento)
        print(f"Tweet {i+1}/{min(len(tweets), max_tweets)}: {sentimiento}")

    return sentimientos
