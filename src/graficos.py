"""
(graficos.py) Este archivo se encarga de CREAR GRÁFICOS interactivos.

Usa Plotly para crear:
1. Gráfico de pastel (distribución de sentimientos)
2. Gráfico de barras (conteo de emociones)
3. Gráfico de línea de tiempo (evolución temporal)
4. Nube de palabras (palabras más frecuentes)
5. Gráfico de caja (distribución de Longitud)
6. Gráfico de bigotes (violin plot)
7. Gráfico de escalera (step chart)
8. Histograma (distribución de Longitud de tweets)
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io


# Colores llamativos para cada sentimiento (pensado para jóvenes)
COLORES_SENTIMIENTOS = {
    "Asustado": "#9b59b6",    # Morado
    "Enojado": "#e74c3c",     # Rojo
    "Triste": "#3498db",      # Azul
    "Tranquilo": "#1abc9c",   # Turquesa
    "Poderoso": "#f39c12",    # Naranja
    "Alegre": "#2ecc71",      # Verde
    "Neutral": "#95a5a6",     # Gris
}


def _obtener_columna_sentimiento(df: pd.DataFrame) -> str:
    """Determina qué columna de sentimiento usar."""
    if "sentimiento_gemini" in df.columns:
        return "sentimiento_gemini"
    return "sentimiento"


def crear_grafico_pastel(df: pd.DataFrame) -> go.Figure:
    """Gráfico de pastel mostrando la distribución de sentimientos."""
    columna = _obtener_columna_sentimiento(df)
    conteo = df[columna].value_counts()

    fig = px.pie(
        values=conteo.values,
        names=conteo.index,
        title="Distribución de Sentimientos",
        color_discrete_map=COLORES_SENTIMIENTOS,
        hole=0.3,
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    fig.update_layout(title_x=0.5, title_font_size=20, font_size=14)
    return fig


def crear_grafico_barras(df: pd.DataFrame) -> go.Figure:
    """Gráfico de barras mostrando cuántos tweets hay por sentimiento."""
    columna = _obtener_columna_sentimiento(df)
    conteo = df[columna].value_counts().reset_index()
    conteo.columns = ["Sentimiento", "Cantidad"]

    fig = px.bar(
        conteo,
        x="Sentimiento",
        y="Cantidad",
        title="Conteo de Tweets por Sentimiento",
        color="Sentimiento",
        color_discrete_map=COLORES_SENTIMIENTOS,
        text="Cantidad",
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(
        title_x=0.5, title_font_size=20,
        xaxis_title="Sentimiento", yaxis_title="Número de Tweets",
        font_size=14, showlegend=False,
    )
    return fig


def crear_grafico_linea_tiempo(df: pd.DataFrame) -> go.Figure:
    """Gráfico de línea de tiempo mostrando la evolución de sentimientos."""
    columna = _obtener_columna_sentimiento(df)
    columna_fecha = None
    for col in ["fecha", "date", "timestamp", "created_at"]:
        if col in df.columns:
            columna_fecha = col
            break

    if columna_fecha:
        datos = df.groupby([columna_fecha, columna]).size().reset_index(name="Cantidad")
        eje_x = columna_fecha
    else:
        df_temp = df.copy()
        df_temp["orden"] = range(1, len(df_temp) + 1)
        datos = df_temp.groupby(["orden", columna]).size().reset_index(name="Cantidad")
        eje_x = "orden"

    fig = px.line(
        datos, x=eje_x, y="Cantidad", color=columna,
        title="Evolución de Sentimientos en el Tiempo",
        color_discrete_map=COLORES_SENTIMIENTOS, markers=True,
    )
    fig.update_layout(
        title_x=0.5, title_font_size=20,
        xaxis_title="Tiempo (orden)" if not columna_fecha else "Fecha",
        yaxis_title="Número de Tweets", font_size=14,
    )
    return fig


def crear_nube_palabras(df: pd.DataFrame, sentimiento: str = None):
    """Nube de palabras con las palabras más frecuentes en los tweets."""
    df_temp = df.copy()
    if sentimiento and sentimiento != "Todos":
        columna = _obtener_columna_sentimiento(df_temp)
        df_temp = df_temp[df_temp[columna].str.contains(sentimiento, case=False, na=False)]

    texto = " ".join(df_temp["tweet"].dropna().astype(str))

    if not texto.strip():
        return None

    nube = WordCloud(
        width=900, height=450,
        background_color="white",
        colormap="plasma",
        max_words=100,
        prefer_horizontal=0.7,
        min_font_size=10,
    ).generate(texto)

    img_buf = io.BytesIO()
    fig_mpl, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(nube, interpolation="bilinear")
    ax.axis("off")
    ax.set_facecolor("white")
    fig_mpl.patch.set_facecolor("white")
    plt.savefig(img_buf, format="png", bbox_inches="tight", dpi=100, facecolor="white")
    plt.close(fig_mpl)
    img_buf.seek(0)

    return img_buf


def crear_grafico_caja(df: pd.DataFrame) -> go.Figure:
    """Gráfico de caja mostrando la distribución de longitud de tweets por sentimiento."""
    columna = _obtener_columna_sentimiento(df)
    df_temp = df.copy()
    df_temp["longitud_tweet"] = df_temp["tweet"].astype(str).str.len()

    fig = px.box(
        df_temp, x=columna, y="longitud_tweet",
        title="Distribución de Longitud de Tweets por Sentimiento",
        color=columna, color_discrete_map=COLORES_SENTIMIENTOS,
    )
    fig.update_layout(
        title_x=0.5, title_font_size=20,
        xaxis_title="Sentimiento", yaxis_title="Longitud del Tweet (caracteres)",
        font_size=14, showlegend=False,
    )
    return fig


def crear_grafico_bigotes(df: pd.DataFrame) -> go.Figure:
    """Gráfico de bigotes (violin plot) mostrando densidad de longitud por sentimiento."""
    columna = _obtener_columna_sentimiento(df)
    df_temp = df.copy()
    df_temp["longitud_tweet"] = df_temp["tweet"].astype(str).str.len()

    fig = px.violin(
        df_temp, x=columna, y="longitud_tweet",
        title="Densidad de Longitud de Tweets por Sentimiento (Violin Plot)",
        color=columna, color_discrete_map=COLORES_SENTIMIENTOS,
        box=True, points="outliers",
    )
    fig.update_layout(
        title_x=0.5, title_font_size=20,
        xaxis_title="Sentimiento", yaxis_title="Longitud del Tweet (caracteres)",
        font_size=14, showlegend=False,
    )
    return fig


def crear_grafico_escalera(df: pd.DataFrame) -> go.Figure:
    """Gráfico de escalera (step chart) mostrando la acumulación de tweets por sentimiento."""
    columna = _obtener_columna_sentimiento(df)
    sentimientos_unicos = df[columna].unique()

    fig = go.Figure()

    colores_lista = [
        COLORES_SENTIMIENTOS.get(s, "#95a5a6") for s in sentimientos_unicos
    ]

    for i, sent in enumerate(sentimientos_unicos):
        df_sent = df[df[columna] == sent].reset_index(drop=True)
        df_sent["acumulado"] = range(1, len(df_sent) + 1)
        fig.add_trace(go.Scatter(
            x=df_sent.index, y=df_sent["acumulado"],
            mode="lines", name=sent,
            line=dict(width=2, color=colores_lista[i]),
            line_shape="hv",
        ))

    fig.update_layout(
        title="Acumulación de Tweets por Sentimiento (Escalera)",
        title_x=0.5, title_font_size=20,
        xaxis_title="Número de Tweet", yaxis_title="Tweets Acumulados",
        font_size=14, legend_title="Sentimiento",
    )
    return fig


def crear_histograma(df: pd.DataFrame) -> go.Figure:
    """Histograma mostrando la distribución de la longitud de los tweets."""
    columna = _obtener_columna_sentimiento(df)
    df_temp = df.copy()
    df_temp["longitud_tweet"] = df_temp["tweet"].astype(str).str.len()

    fig = px.histogram(
        df_temp, x="longitud_tweet", color=columna,
        title="Distribución de Longitud de Todos los Tweets",
        color_discrete_map=COLORES_SENTIMIENTOS,
        nbins=30, barmode="overlay", opacity=0.7,
    )
    fig.update_layout(
        title_x=0.5, title_font_size=20,
        xaxis_title="Longitud del Tweet (caracteres)",
        yaxis_title="Cantidad de Tweets",
        font_size=14, legend_title="Sentimiento",
    )
    return fig
