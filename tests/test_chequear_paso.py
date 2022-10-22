from src.othello import chequear_paso

def test_chequear_paso():
  tablero0 = [[2, 2, 2, 2, 2, 2, 2, 1],
              [0, 0, 1, 1, 1, 2, 2, 2],
              [0, 1, 1, 2, 1, 2, 2, 2],
              [1, 1, 1, 2, 1, 2, 2, 2],
              [1, 1, 2, 1, 2, 1, 2, 2],
              [1, 2, 1, 2, 2, 2, 2, 2],
              [2, 2, 2, 1, 2, 2, 1, 2],
              [1, 1, 1, 1, 2, 2, 1, 2]]

  tablero1 = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 2, 0, 0, 0],
              [0, 0, 0, 2, 2, 2, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]

  assert True == chequear_paso(tablero0,1)
  assert False == chequear_paso(tablero0,2)
  assert False == chequear_paso(tablero1,1)
  assert False == chequear_paso(tablero1,2)