"""
(app.py) Archivo principal del dashboard - Vibe Check IA

Dashboard interactivo que analiza sentimientos de tweets en español
usando pysentimiento (análisis local, sin API key).
"""

import streamlit as st
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from datos import leer_csv, limpiar_datos, filtrar_por_sentimiento, obtener_sentimientos_unicos
from graficos import (
    crear_grafico_pastel, crear_grafico_barras, crear_grafico_linea_tiempo,
    crear_nube_palabras, crear_grafico_caja, crear_grafico_bigotes,
    crear_grafico_escalera, crear_histograma,
)
from analizador import clasificar_sentimiento


st.set_page_config(
    page_title="Vibe Check IA - Analizador de Sentimientos",
    page_icon="🎭",
    layout="wide"
)


def main():
    st.title("🎭 Vibe Check IA: Analizador de Sentimientos en Twitter")
    st.markdown("""
    Analiza el sentimiento de tweets en español usando **Inteligencia Artificial** local.
    Selecciona un filtro y presiona el botón para analizar.

    **Dataset:** [Twitter Sentiment Analysis in Spanish Tweets](https://www.kaggle.com/datasets/philipsanm/sentiment-analysis-in-spanish-tweets)
    """)

    with st.sidebar:
        st.header("⚙️ Configuración")

        ruta_csv = "data/sentiment_analysis_dataset.csv"

        if not os.path.exists(ruta_csv):
            st.error(
                "No se encontró el archivo CSV.\n\n"
                "**Pasos para solucionarlo:**\n"
                "1. Descarga el dataset de [Kaggle](https://www.kaggle.com/datasets/philipsanm/sentiment-analysis-in-spanish-tweets)\n"
                "2. Renómbralo a `sentiment_analysis_dataset.csv`\n"
                "3. Colócalo en la carpeta `data/`"
            )
            st.stop()

        try:
            df = leer_csv(ruta_csv)
            df = limpiar_datos(df)
            st.success(f"Dataset cargado: {len(df)} tweets")
        except Exception as e:
            st.error(f"Error al cargar el dataset: {e}")
            st.stop()

        sentimientos = obtener_sentimientos_unicos(df)

        sentimiento_seleccionado = st.selectbox(
            "🔍 Selecciona un sentimiento:",
            sentimientos,
            index=0
        )

        max_tweets = st.slider(
            "📊 Máximo de tweets a analizar:",
            min_value=1,
            max_value=50,
            value=10,
        )

        analizar_ia = st.checkbox(
            "🤖 Analizar con IA (pysentimiento)",
            value=False,
        )

    df_filtrado = filtrar_por_sentimiento(df, sentimiento_seleccionado)

    if st.button("Analizar Tweets", type="primary", use_container_width=True):

        if analizar_ia:
            with st.spinner("Analizando tweets con IA... esto puede tardar unos segundos"):
                tweets_para_analizar = df_filtrado["tweet"].tolist()
                sentimientos_ia = []

                for tweet in tweets_para_analizar[:max_tweets]:
                    sentimiento = clasificar_sentimiento(tweet)
                    sentimientos_ia.append(sentimiento)

                df_filtrado["sentimiento_gemini"] = sentimientos_ia

            st.success(f"Análisis completado para {len(sentimientos_ia)} tweets")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total de Tweets", len(df_filtrado))
        with col2:
            st.metric(
                "😄 Alegres",
                len(df_filtrado[df_filtrado["sentimiento"].str.contains("Alegre", case=False, na=False)])
            )
        with col3:
            st.metric(
                "😢 Tristes",
                len(df_filtrado[df_filtrado["sentimiento"].str.contains("Triste", case=False, na=False)])
            )

    # ═══════════════════════════════════════════════════════════
    # GRÁFICOS
    # ═══════════════════════════════════════════════════════════

    # --- GRÁFICO 1: Pastel ---
    st.markdown("---")
    st.subheader("🥧 Distribución de Sentimientos")
    st.markdown("Proporción de cada emoción en el dataset. Cuanto más grande la porción, más tweets tienen ese sentimiento.")
    fig_pastel = crear_grafico_pastel(df_filtrado)
    st.plotly_chart(fig_pastel, use_container_width=True)

    # --- GRÁFICO 2: Barras ---
    st.markdown("---")
    st.subheader("📊 Conteo de Tweets por Sentimiento")
    st.markdown("Cantidad exacta de tweets clasificados en cada categoría de emoción.")
    fig_barras = crear_grafico_barras(df_filtrado)
    st.plotly_chart(fig_barras, use_container_width=True)

    # --- GRÁFICO 3: Línea de tiempo ---
    st.markdown("---")
    st.subheader("📈 Evolución de Sentimientos en el Tiempo")
    st.markdown("Cómo cambian los sentimientos a lo largo de la secuencia de tweets.")
    fig_linea = crear_grafico_linea_tiempo(df_filtrado)
    st.plotly_chart(fig_linea, use_container_width=True)

    # --- GRÁFICO 4: Nube de palabras ---
    st.markdown("---")
    st.subheader("☁️ Nube de Palabras Más Frecuentes")
    st.markdown("Las palabras más utilizadas en los tweets. Las palabras más grandes son las que aparecen con más frecuencia.")
    img_nube = crear_nube_palabras(df_filtrado, sentimiento_seleccionado)
    if img_nube:
        st.image(img_nube, use_container_width=True)
    else:
        st.warning("No hay texto suficiente para generar la nube de palabras.")

    # --- GRÁFICO 5: Caja (Box Plot) ---
    st.markdown("---")
    st.subheader("📦 Distribución de Longitud de Tweets (Caja)")
    st.markdown("Muestra la mediana, cuartiles y valores atípicos de la longitud de los tweets por sentimiento.")
    fig_caja = crear_grafico_caja(df_filtrado)
    st.plotly_chart(fig_caja, use_container_width=True)

    # --- GRÁFICO 6: Bigotes (Violin Plot) ---
    st.markdown("---")
    st.subheader("🎻 Densidad de Longitud de Tweets (Bigotes)")
    st.markdown("Muestra la distribución de densidad de la longitud de tweets por sentimiento, como una versión extendida del gráfico de caja.")
    fig_bigotes = crear_grafico_bigotes(df_filtrado)
    st.plotly_chart(fig_bigotes, use_container_width=True)

    # --- GRÁFICO 7: Escalera (Step Chart) ---
    st.markdown("---")
    st.subheader("🪜 Acumulación de Tweets por Sentimiento (Escalera)")
    st.markdown("Muestra cómo se acumulan los tweets de cada sentimiento a lo largo del tiempo.")
    fig_escalera = crear_grafico_escalera(df_filtrado)
    st.plotly_chart(fig_escalera, use_container_width=True)

    # --- GRÁFICO 8: Histograma ---
    st.markdown("---")
    st.subheader("📉 Distribución de Longitud de Todos los Tweets")
    st.markdown("Histograma que muestra cuántos tweets tienen cada longitud, desglosados por sentimiento.")
    fig_histograma = crear_histograma(df_filtrado)
    st.plotly_chart(fig_histograma, use_container_width=True)

    # --- Tabla de datos ---
    with st.expander("Ver datos en tabla", expanded=False):
        st.dataframe(
            df_filtrado[["tweet", "sentimiento"]].head(100),
            use_container_width=True
        )

    st.markdown("---")
    st.markdown(
        "Desarrollado con Python, Streamlit, Plotly y pysentimiento | "
        "Dataset: [Kaggle - Twitter Sentiment in Spanish](https://www.kaggle.com/datasets/philipsanm/sentiment-analysis-in-spanish-tweets)"
    )


if __name__ == "__main__":
    main()
