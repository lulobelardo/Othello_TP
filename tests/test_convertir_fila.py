from src.othello import convertir_fila

def test_convertir_fila():
    caracteres = '0123456789'
    caracteres1 = 'AHSR.`J'
    assert -1 == convertir_fila(caracteres[0])
    assert 0 == convertir_fila(caracteres[1])
    assert 1 == convertir_fila(caracteres[2])
    assert 2 == convertir_fila(caracteres[3])
    assert 3 == convertir_fila(caracteres[4])
    assert 4 == convertir_fila(caracteres[5])
    assert 5 == convertir_fila(caracteres[6])
    assert 6 == convertir_fila(caracteres[7])
    assert 7 == convertir_fila(caracteres[8])
    assert 8 == convertir_fila(caracteres[9])
    assert -1 ==convertir_fila(caracteres1[0])
    assert -1 ==convertir_fila(caracteres1[1])
    assert -1 ==convertir_fila(caracteres1[2])
    assert -1 ==convertir_fila(caracteres1[3])
    assert -1 ==convertir_fila(caracteres1[4])
    assert -1 ==convertir_fila(caracteres1[5])
    assert -1 ==convertir_fila(caracteres1[6])

