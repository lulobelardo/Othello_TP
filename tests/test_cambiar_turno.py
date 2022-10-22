from src.othello import cambiar_turno

def test_cambiar_turno():
  assert 2 == cambiar_turno(1)
  assert 1 == cambiar_turno(2)