"""
(test_graficos.py) Tests automatizados para el módulo graficos.py

Verifica que se puedan crear todos los tipos de gráficos sin errores.
"""

import pytest
import pandas as pd
import plotly.graph_objects as go

from src.graficos import (
    crear_grafico_pastel,
    crear_grafico_barras,
    crear_grafico_linea_tiempo,
    crear_nube_palabras,
    crear_grafico_caja,
    crear_grafico_bigotes,
    crear_grafico_escalera,
    crear_histograma,
)


# ============================================================
# FUNCIÓN AUXILIAR: Crear DataFrame de prueba
# ============================================================
def crear_df_prueba() -> pd.DataFrame:
    """Crea un DataFrame ficticio con tweets y sentimientos para los tests."""
    datos = {
        "tweet": [
            "Estoy muy feliz hoy",
            "Qué día tan horrible",
            "Hoy es martes",
            "¡Me encanta la pizza!",
            "Odio el tráfico",
            "El cielo está azul",
            "No me gusta la lluvia",
            "Buenos días a todos"
        ],
        "sentimiento": [
            "Alegre",
            "Triste",
            "Tranquilo",
            "Alegre",
            "Triste",
            "Alegre",
            "Triste",
            "Tranquilo"
        ]
    }
    return pd.DataFrame(datos)


# ============================================================
# TEST: Gráfico de pastel
# ============================================================
def test_crear_grafico_pastel():
    df = crear_df_prueba()
    fig = crear_grafico_pastel(df)

    assert isinstance(fig, go.Figure), "crear_grafico_pastel debe devolver un objeto go.Figure"
    assert len(fig.data) > 0, "El gráfico debe tener al menos una traza"
    assert fig.layout.title.text is not None, "El gráfico debe tener un título"
    assert len(fig.data[0].labels) > 0, "El gráfico debe tener etiquetas"


# ============================================================
# TEST: Gráfico de barras
# ============================================================
def test_crear_grafico_barras():
    df = crear_df_prueba()
    fig = crear_grafico_barras(df)

    assert isinstance(fig, go.Figure), "crear_grafico_barras debe devolver un objeto go.Figure"
    assert len(fig.data) > 0, "El gráfico debe tener al menos una traza"
    assert fig.layout.title.text is not None, "El gráfico debe tener un título"


# ============================================================
# TEST: Gráfico de línea de tiempo
# ============================================================
def test_crear_grafico_linea_tiempo():
    df = crear_df_prueba()
    fig = crear_grafico_linea_tiempo(df)

    assert isinstance(fig, go.Figure), "crear_grafico_linea_tiempo debe devolver un objeto go.Figure"
    assert len(fig.data) > 0, "El gráfico debe tener al menos una traza"
    assert fig.layout.title.text is not None, "El gráfico debe tener un título"


# ============================================================
# TEST: Gráfico de caja
# ============================================================
def test_crear_grafico_caja():
    df = crear_df_prueba()
    fig = crear_grafico_caja(df)

    assert isinstance(fig, go.Figure), "crear_grafico_caja debe devolver un objeto go.Figure"
    assert len(fig.data) > 0, "El gráfico debe tener al menos una traza"
    assert fig.layout.title.text is not None, "El gráfico debe tener un título"


# ============================================================
# TEST: Gráfico de bigotes (violin)
# ============================================================
def test_crear_grafico_bigotes():
    df = crear_df_prueba()
    fig = crear_grafico_bigotes(df)

    assert isinstance(fig, go.Figure), "crear_grafico_bigotes debe devolver un objeto go.Figure"
    assert len(fig.data) > 0, "El gráfico debe tener al menos una traza"
    assert fig.layout.title.text is not None, "El gráfico debe tener un título"


# ============================================================
# TEST: Gráfico de escalera (step)
# ============================================================
def test_crear_grafico_escalera():
    df = crear_df_prueba()
    fig = crear_grafico_escalera(df)

    assert isinstance(fig, go.Figure), "crear_grafico_escalera debe devolver un objeto go.Figure"
    assert len(fig.data) > 0, "El gráfico debe tener al menos una traza"
    assert fig.layout.title.text is not None, "El gráfico debe tener un título"


# ============================================================
# TEST: Histograma
# ============================================================
def test_crear_histograma():
    df = crear_df_prueba()
    fig = crear_histograma(df)

    assert isinstance(fig, go.Figure), "crear_histograma debe devolver un objeto go.Figure"
    assert len(fig.data) > 0, "El gráfico debe tener al menos una traza"
    assert fig.layout.title.text is not None, "El gráfico debe tener un título"


# ============================================================
# TEST: Nube de palabras
# ============================================================
def test_crear_nube_palabras():
    df = crear_df_prueba()
    resultado = crear_nube_palabras(df)

    # La función devuelve un BytesIO o None
    if resultado is not None:
        assert hasattr(resultado, "getvalue"), "La nube debe devolver un BytesIO"


# ============================================================
# TEST: Gráficos con DataFrame vacío
# ============================================================
def test_grafico_dataframe_vacio():
    """Verifica que los gráficos no crashean con un DataFrame vacío."""
    df_vacio = pd.DataFrame(columns=["tweet", "sentimiento"])

    fig_pastel = crear_grafico_pastel(df_vacio)
    assert isinstance(fig_pastel, go.Figure), "El gráfico de pastel debe funcionar con DataFrame vacío"

    fig_barras = crear_grafico_barras(df_vacio)
    assert isinstance(fig_barras, go.Figure), "El gráfico de barras debe funcionar con DataFrame vacío"

    fig_linea = crear_grafico_linea_tiempo(df_vacio)
    assert isinstance(fig_linea, go.Figure), "El gráfico de línea debe funcionar con DataFrame vacío"

    fig_caja = crear_grafico_caja(df_vacio)
    assert isinstance(fig_caja, go.Figure), "El gráfico de caja debe funcionar con DataFrame vacío"

    fig_bigotes = crear_grafico_bigotes(df_vacio)
    assert isinstance(fig_bigotes, go.Figure), "El gráfico de bigotes debe funcionar con DataFrame vacío"

    fig_escalera = crear_grafico_escalera(df_vacio)
    assert isinstance(fig_escalera, go.Figure), "El gráfico de escalera debe funcionar con DataFrame vacío"

    fig_histograma = crear_histograma(df_vacio)
    assert isinstance(fig_histograma, go.Figure), "El histograma debe funcionar con DataFrame vacío"
