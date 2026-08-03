"""
(test_datos.py) Tests automatizados para el módulo datos.py

Verifica:
- Lectura de CSV
- Limpieza de datos
- Filtrado por sentimiento (sentimientos en español)
- Obtención de sentimientos únicos
"""

import pytest
import os
import tempfile
import pandas as pd

from src.datos import (
    leer_csv,
    limpiar_datos,
    filtrar_por_sentimiento,
    obtener_sentimientos_unicos,
    TRADUCCION_SENTIMIENTOS,
)


# ============================================================
# TEST T1: Verificar que el CSV se lee correctamente
# ============================================================
def test_leer_csv_existe(tmp_path):
    """
    TEST T1: Verifica que leer_csv() puede leer un archivo CSV real.
    """
    datos_prueba = "tweet,sentimiento\nHoy hace sol,joyful\nEstoy triste,sad\n"
    ruta_csv = tmp_path / "test_tweets.csv"
    ruta_csv.write_text(datos_prueba, encoding="utf-8")

    df = leer_csv(str(ruta_csv))

    assert isinstance(df, pd.DataFrame), "leer_csv debe devolver un DataFrame"
    assert len(df) == 2, f"El CSV debe tener 2 filas, pero tiene {len(df)}"
    assert "tweet" in df.columns, "El DataFrame debe tener una columna 'tweet'"
    assert "sentimiento" in df.columns, "El DataFrame debe tener una columna 'sentimiento'"


# ============================================================
# TEST T2: Verificar que el CSV tiene las columnas esperadas
# ============================================================
def test_csv_tiene_columnas_esperadas(tmp_path):
    """
    TEST T2: Verifica que el CSV tiene las columnas 'tweet' y 'sentimiento'.
    """
    datos_prueba = "tweet,sentimiento\nMe encanta este día,joyful\nNo me gusta nada,sad\n"
    ruta_csv = tmp_path / "test_columnas.csv"
    ruta_csv.write_text(datos_prueba, encoding="utf-8")

    df = leer_csv(str(ruta_csv))

    columnas_necesarias = ["tweet", "sentimiento"]
    for columna in columnas_necesarias:
        assert columna in df.columns, f"Falta la columna '{columna}' en el CSV"


# ============================================================
# TEST T3: Verificar que el filtro de sentimientos funciona
# ============================================================
def test_filtrar_por_sentimiento():
    """
    TEST T3: Verifica que filtrar_por_sentimiento() devuelve solo los tweets correctos.
    """
    datos = {
        "tweet": [
            "Estoy muy feliz hoy",
            "Qué día tan horrible",
            "Hoy es martes",
            "¡Me encanta la pizza!",
            "Odio el tráfico"
        ],
        "sentimiento": [
            "Alegre",
            "Triste",
            "Tranquilo",
            "Alegre",
            "Triste"
        ]
    }
    df = pd.DataFrame(datos)

    # CASO 1: Filtrar solo alegres.
    df_alegres = filtrar_por_sentimiento(df, "Alegre")
    assert len(df_alegres) == 2, f"Debería haber 2 alegres, hay {len(df_alegres)}"
    assert all(df_alegres["sentimiento"] == "Alegre"), "Todos los filtrados deben ser Alegre"

    # CASO 2: Filtrar solo tristes.
    df_tristes = filtrar_por_sentimiento(df, "Triste")
    assert len(df_tristes) == 2, f"Debería haber 2 tristes, hay {len(df_tristes)}"

    # CASO 3: Filtrar "Todos" debe devolver el DataFrame completo.
    df_todos = filtrar_por_sentimiento(df, "Todos")
    assert len(df_todos) == 5, "Filtrar 'Todos' debe devolver todos los tweets"


# ============================================================
# TEST T4: Verificar que un tweet vacío no rompe el programa
# ============================================================
def test_tweet_vacio_no_rompe():
    """
    TEST T4: Verifica que tweets vacíos no hacen crashear el programa.
    """
    datos = {
        "tweet": [
            "Tweet normal",
            "",
            "   ",
            None,
            "Otro tweet normal"
        ],
        "sentimiento": [
            "Alegre",
            "Tranquilo",
            "Triste",
            "Alegre",
            "Triste"
        ]
    }
    df = pd.DataFrame(datos)

    df_limpio = limpiar_datos(df)

    assert len(df_limpio) == 2, f"Deberían quedar 2 tweets válidos, quedan {len(df_limpio)}"
    assert all(df_limpio["tweet"].str.strip() != ""), "No deben quedar tweets vacíos"


# ============================================================
# TEST EXTRA: Verificar que obtener_sentimientos_unicos funciona
# ============================================================
def test_obtener_sentimientos_unicos():
    """
    TEST EXTRA: Verifica que obtener_sentimientos_unicos() devuelve la lista correcta.
    """
    datos = {
        "tweet": ["a", "b", "c", "d"],
        "sentimiento": ["Alegre", "Triste", "Tranquilo", "Alegre"]
    }
    df = pd.DataFrame(datos)

    sentimientos = obtener_sentimientos_unicos(df)

    assert sentimientos[0] == "Todos", "El primer elemento debe ser 'Todos'"
    assert "Alegre" in sentimientos
    assert "Triste" in sentimientos
    assert "Tranquilo" in sentimientos


# ============================================================
# TEST EXTRA: Verificar que la traducción funciona
# ============================================================
def test_traduccion_sentimientos():
    """
    TEST EXTRA: Verifica que TRADUCCION_SENTIMIENTOS tenga las traducciones correctas.
    """
    assert TRADUCCION_SENTIMIENTOS["scared"] == "Asustado"
    assert TRADUCCION_SENTIMIENTOS["mad"] == "Enojado"
    assert TRADUCCION_SENTIMIENTOS["sad"] == "Triste"
    assert TRADUCCION_SENTIMIENTOS["peaceful"] == "Tranquilo"
    assert TRADUCCION_SENTIMIENTOS["powerful"] == "Poderoso"
    assert TRADUCCION_SENTIMIENTOS["joyful"] == "Alegre"
