from src.othello import copiar_tablero

def test_copiar_tablero():
  tablero_1 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 2, 0, 0, 0, 0],
               [0, 0, 0, 2, 2, 0, 0, 0],
               [0, 0, 0, 2, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]
  tablero_2 = tablero_1
  assert (tablero_2 is tablero_1) == True

  tablero_2 = copiar_tablero(tablero_1)
  assert tablero_2 == tablero_1
  assert (tablero_2 is tablero_1) == False

  tablero_1 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]
  assert tablero_2 != tablero_1

  tablero_2 = [[2, 2, 2, 2, 2, 2, 1, 2],
               [2, 2, 2, 2, 2, 2, 1, 2],
               [2, 2, 2, 2, 2, 1, 1, 2],
               [2, 2, 1, 2, 1, 2, 1, 2],
               [2, 2, 2, 1, 1, 2, 2, 2],
               [2, 2, 1, 2, 2, 1, 2, 2],
               [2, 1, 2, 2, 2, 1, 1, 2],
               [1, 1, 1, 1, 1, 1, 1, 1]]
  tablero_3 = tablero_2
  assert (tablero_3 is tablero_2) == True

  tablero_3 = copiar_tablero(tablero_2)
  assert tablero_3 == tablero_2
  assert (tablero_3 is tablero_2) == False

  tablero_3 = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]
  assert tablero_3 != tablero_2