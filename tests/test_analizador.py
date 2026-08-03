"""
(test_analizador.py) Tests automatizados para el módulo analizador.py

Usa pysentimiento (análisis local, sin API key).
Verifica que la clasificación de sentimientos funcione correctamente.
"""

import pytest
from unittest.mock import patch, MagicMock
from src.analizador import clasificar_sentimiento, MAPEO_SENTIMIENTOS, NEUTRAL


# ============================================================
# TEST T5: Verificar que clasificar_sentimiento devuelve un valor válido
# ============================================================
def test_clasificar_sentimiento_valor_valido():
    """
    TEST T5: Verifica que clasificar_sentimiento() devuelve un sentimiento del mapeo.
    """
    resultado = clasificar_sentimiento("Me encanta este día, es maravilloso")

    assert resultado in MAPEO_SENTIMIENTOS.values() or resultado == NEUTRAL, \
        f"El resultado '{resultado}' no es un sentimiento válido"


# ============================================================
# TEST T6: Verificar que el mapeo de sentimientos tiene las claves correctas
# ============================================================
def test_mapeo_sentimientos_completo():
    """
    TEST T6: Verifica que MAPEO_SENTIMIENTOS tenga todas las categorías esperadas.
    """
    esperados = {"scared", "mad", "sad", "peaceful", "powerful", "joyful"}
    assert set(MAPEO_SENTIMIENTOS.keys()) == esperados, \
        "MAPEO_SENTIMIENTOS no tiene las claves correctas"


# ============================================================
# TEST T7: Verificar que NEUTRAL sea una cadena no vacía
# ============================================================
def test_neutral_definido():
    """
    TEST T7: Verifica que NEUTRAL esté definido correctamente.
    """
    assert isinstance(NEUTRAL, str), "NEUTRAL debe ser una cadena"
    assert len(NEUTRAL) > 0, "NEUTRAL no puede estar vacío"


# ============================================================
# TEST T8: Verificar que un error de conexión no crashea
# ============================================================
def test_manejo_error_conexion():
    """
    TEST T8: Verifica que si pysentimiento falla, el programa NO se crashea.
    """
    with patch("src.analizador.obtener_analizador") as mock_analizador:
        mock_analizador.side_effect = Exception("Error de modelo")

        resultado = clasificar_sentimiento("Tweet de prueba")

        assert resultado == NEUTRAL, \
            "Si el analizador falla, la función debe devolver NEUTRAL como valor seguro"
