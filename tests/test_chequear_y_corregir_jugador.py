from src.othello import chequear_y_corregir_jugador

def test_chequear_y_corregir_jugador():
    jugador1 = ['Luciano Belardo', '  N     ']
    jugador2 = ['Ignacio Basualdo', 'S']
    jugador3 = ['Luciano Belardo', 'N', 'mayonesa']

    assert chequear_y_corregir_jugador(jugador1) == ['Luciano Belardo','N']
    assert chequear_y_corregir_jugador(jugador2) == []
    assert chequear_y_corregir_jugador(jugador3) == []