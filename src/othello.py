'''
Tablero := List(List(Int))
1 := B (Blancas)
2 := N (Negras)
'''

# crear_tablero: None -> Tablero
# Retorna el tablero inicial
def crear_tablero():
  return [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 2, 0, 0, 0],
          [0, 0, 0, 2, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]]

# copiar_tablero: Tablero -> Tablero
# Retorna una copia no referenciada del tablero
'''
Toma un tablero.
La funcion crea una matriz nueva, y luego copia -sin referenciar- cada fila del
tablero original en copia_tablero, así modificar uno no modifica el otro.
'''
def copiar_tablero(tablero):
  copia_tablero = [[], [], [], [], [], [], [], []]
  for indice, fila in enumerate(tablero):
    copia_tablero[indice] = fila[:]
  return copia_tablero

# chequear_paso: Tablero, Int -> Bool
# Retorna True si es válido que el jugador 'pase', caso contrario retorna False
'''
Toma como parámetros el tablero y de quien es el turno.
Para ver si pasar es válido, la funcion chequea si efectivamente ninguno de los
64 movimientos posibles es válido, caso en el que 'pasar' es correcto.
Si tan solo 1 movimiento es válido, entonces 'pasar' es incorrecto, termina de
hacer chequeos y retorna falso.
'''
def chequear_paso(tablero, turno):
  # Para no modificar el tablero original
  copia_tablero = copiar_tablero(tablero)
  
  continuar = True
  fila = 0
  while fila < 8 and continuar:
    columna = 0
    while columna < 8 and continuar:
      continuar = not realizar_jugada(copia_tablero, (fila, columna), turno)
      columna += 1 
    fila += 1
  return continuar

# modificar_tablero: Tablero, (Int, Int), Int, Int -> None
# Modifica segun la direccion indicada los valores del tablero correspondientes
'''
Toma como parametros el tablero, la posicion jugada (VALIDA), de quien es el
turno y la direccion que quiero modificar (8 posibles).
La funcion hace el movimiento COMPLETO en una direccion indicada, es decir,
voltea todas las fichas correspondientes en una direccion siempre y cuando haya
fichas que voltear.
El parámetro 'direccion' es una tupla de dos numeros que pueden ser -1, 0 y 1.
Los mismos reflejan la direccion fila/columna en la que me estoy desplazando
respectivamente. La direccion (0, 0) no existe.
'''
def modificar_tablero(tablero, jugada, turno, direccion):
  # Asignaciones
  j_fila = jugada[0] # jugada_fila
  j_colum = jugada[1] # jugada_columna
  vert = direccion[0] # Vertical: variacion en las filas
  horiz = direccion[1] # Horizontal: variacion en las columnas
  
  delta_final = 0 # Representa la cantidad final de fichas a voltear
  delta = 1 # Contador de fichas a cambiar
  
  continuar = True
  while continuar:
    # Caso en el que la jugada se salga del tablero
    if (j_fila + delta * vert not in range(8) or
        j_colum + delta * horiz not in range(8)): 
      continuar = False
    elif delta == 1: # Solo si es adyacente a la jugada
      # Caso que haya una ficha del mismo color o no hay ninguna ficha
      if tablero[j_fila + delta * vert][j_colum + delta * horiz] in (0, turno):
        continuar = False
    # Caso que no haya ninguna ficha
    elif tablero[j_fila + delta * vert][j_colum + delta * horiz] == 0:
      continuar = False
    # Caso que haya una ficha del mismo color LUEGO de una o mas del otro color
    elif tablero[j_fila + delta * vert][j_colum + delta * horiz] == turno:
      delta_final = delta # Se va a modificar el tablero delta lugares
      continuar = False
    # Desplazo delta para analizar la siguiente posicion 
    delta += 1
  
  # Cambiar el color de las fichas encerradas (delta_final lugares)
  for lugar in range(1, delta_final):
    tablero[j_fila + lugar * vert][j_colum + lugar * horiz] = turno

# realizar_jugada: Tablero, (Int, Int), Int -> Bool
# Si la jugada es válida, retorna True y la realiza, sino, retorna False
'''
Toma como parametros el tablero, la jugada y el turno.
Si la jugada es inválida, retorna False y no modifica el tablero,
si en un principio la jugada es válida, entonces modifica el tablero segun
corresponda en todas las direcciones, y si al hacerlo el tablero se modificó,
entonces la jugada era efectivamente válida, la realiza y retorna True. Por
otro lado, si el tablero NO se modificó, entonces la jugada era inválida, por
lo que retorna False.
'''
def realizar_jugada(tablero, jugada, turno):
  # Caso jugada fuera de rango
  if jugada[0] not in range(8) or jugada[1] not in range(8):
    return False
  # Caso posición ocupada por otra ficha
  if tablero[jugada[0]][jugada[1]] in (1, 2):
    return False

  copia_tablero = copiar_tablero(tablero) # Copia a comparar luego

  # Modifico el tablero en todas las direcciones
  # Derecha
  modificar_tablero(tablero, jugada, turno, (0, 1))
  # Izquierda
  modificar_tablero(tablero, jugada, turno, (0, -1))
  # Arriba
  modificar_tablero(tablero, jugada, turno, (-1, 0))
  # Abajo
  modificar_tablero(tablero, jugada, turno, (1, 0))
  # Diagonal abajo izquierda
  modificar_tablero(tablero, jugada, turno, (1, -1))
  # Diagonal abajo derecha
  modificar_tablero(tablero, jugada, turno, (1, 1))
  # Diagonal arriba derecha
  modificar_tablero(tablero, jugada, turno, (-1, 1))
  # Diagonal arriba izquierda
  modificar_tablero(tablero, jugada, turno, (-1, -1))

  '''
  Notesé que si son iguales, no se modificó por lo que pasar como parámetro el
  tablero original no me afecta. Por otro lado, si se modificó, ya no hace
  falta que se vuelva a modificar, por lo que solo queda poner la ficha.
  '''
  if tablero == copia_tablero: # Si son iguales, la jugada es inválida
    return False

  tablero[jugada[0]][jugada[1]] = turno # Coloco la ficha
  return True

# cambiar_turno: Int -> Int
# Cambia el turno, si era del 1 ahora es del 2, y viceversa
def cambiar_turno(turno):
  return (2 if turno == 1 else 1)

# imprimir_tablero: Tablero -> None
# Imprime el tablero
def imprimir_tablero(tablero):
  print('    A B C D E F G H')
  print('    ---------------')
  for i, fila in enumerate(tablero):
    print(i + 1, end=' | ')
    for valor in fila:
      if valor == 0:
        print('·', end=' ')
      elif valor == 1:
        print('•', end=' ')
      elif valor == 2:
        print('○', end=' ')
    print('|', i + 1)
  print('    ---------------')
  print('    A B C D E F G H')

# contar_fichas: Tablero -> (Int, Int)
'''
Toma el tablero (lleno o no) y retorna una tupla de numeros con la cantidad de
fichas de cada jugador (color) tal que (blancas, negras).
'''
def contar_fichas(tablero):
  blancas = 0 # Contador fichas blancas
  negras = 0 # Contador fichas negras
  # Recorre cada posicion
  for fila in tablero:
    for ficha in fila:
      if ficha == 1: # Es blanca
        blancas += 1
      elif ficha == 2: # Es negra
        negras += 1
  return (blancas, negras)

# resultado: Dict, (Int, Int) -> None
# Muestra en pantalla quien gana segun el puntaje obtenido
'''
Toma un diccionario que contiene ambos jugadores, tal que su clave es su color
('B' o 'N') y el valor es su nombre; y una tupla de enteros que contiene los
puntos del blanco y negro respectivamente.
Imprime en pantalla los puntos de cada jugador y el resultado del juego
(empate, ganan blancas, ganan negras).
'''
def resultado(jugadores, marcador):
  blancas = marcador[0] #Asigna la cantidad de fichas blancas
  negras = marcador[1]  #Asigna la cantidad de fichas negras
  print('Fichas Blancas (' + jugadores['B'] + '): ' + str(blancas)) 
  print('Fichas Negras (' + jugadores['N'] + '): ' + str(negras))
  print() # Estética
  if blancas > negras: # Caso que ganen el jugador con fichas blancas  
    print('Ganan Blancas (' + jugadores['B'] + ').')
  elif negras > blancas: # Caso que ganen el jugador con fichas negras
    print('Ganan Negras (' + jugadores['N'] + ').')
  else: # Caso que haya un empate
    print('Empate')

# tablero_lleno: Tablero -> Bool
# Toma un tablero. Si esta lleno retorna True, caso contrario retorna False
def tablero_lleno(tablero):
  fila = 0
  continuar = True
  # Recorre todas las posiciones mientras haya alguna ficha 
  while fila < 8 and continuar:
    columna = 0 # Reseteo de columnas
    while columna < 8 and continuar:
      if tablero[fila][columna] == 0: # Si hay un lugar vacío
        continuar = False # El tablero no esta lleno
      columna += 1
    fila += 1
  return continuar

# convertir_fila: String -> Int
# Toma un numero como string y retorna el numero como Int - 1
'''
Toma como parametro una string de un caracter (representa la fila). Este
debería ser un dígito.
Si es un entero, retorna el anterior a dicho valor, pues traduce el conteo
'Humano' (comienza por 1) al informático (comienza por 0). Por otra parte, si
es una letra o cualquier otro carater, retorna -1 como aviso de que es erróneo
el dato (si toma '0' tambien es erróneo, por lo que no genera problema).
'''
def convertir_fila(caracter):
  try:
    return int(caracter) - 1
  except ValueError:
    return -1 # El programa sólo verifica que el dato es erróneo luego

# convertir_fila: String -> Int
# Toma una letra como string y retorna el numero de columna correspondiente
'''
Toma como parametro una string de un caracter (representa la columna). Este
debería ser una letra en el rango A-H.
Retorna el valor asociado de cada letra al numero de columna.
Si el dato es erroneo, retorna -1 como aviso del fallo.
'''
def convertir_columna(caracter):
  #Diccionario de columnas con su representacion numerica
  letras = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
  try:
    return letras[caracter]
  except KeyError:
    return -1

# fin_del_juego: Tablero -> Bool
'''
Toma un tablero.
Si no se pueden realizar jugadas retorna True, caso contrario retorna False.
Si ambos pueden pasar con el tablero en dichas condiciones, entonces el juego
termina.
'''
def fin_del_juego(tablero):
  if chequear_paso(tablero,1) and chequear_paso(tablero,2):
    return True
  else:
    return False

def main():
  tablero = crear_tablero() # Se crea el tablero inicial

  f = open('.\src\juego1.txt', 'r') # Se abre el archivo para lectura

  # Guarda cada jugador en una lista con el nombre y con el color de ficha
  jugador1 = f.readline()[:-1].split(',')
  jugador2 = f.readline()[:-1].split(',')
  '''
  Guarda los jugadores en un diccionario cuya clave es el color de la ficha
  y el valor es el nombre del jugador. De la forma:
  {B/N: nombre del jugador1, N/B: nombre del jugador2}
  ''' 
  jugadores = {jugador1[1]: jugador1[0], jugador2[1]: jugador2[0]}

  # Asigna a inicial la letra del color de la ficha que inicia el juego (B\N)
  inicial = f.readline()[:-1]  #FLACO LABURA
  # Traslada ese valor a un número que indica el respectivo turno 
  turno = (1 if inicial == 'B' else 2) # 'B':1, 'N':2
  pasar = 0
  continuar = True
  hay_ganador = False
  while continuar:
    line = f.readline()
    if line: #mientras no sea EOF
      if line != '\n':
        fila = convertir_fila(line[1]) # int(line[1]) - 1
        columna = convertir_columna(line[0]) # letras[line[0]]
        jugada = (fila, columna) #Se pasa la jugada a una tupla numerica (x,y)
        continuar = realizar_jugada(tablero, jugada, turno)
        pasar = 0
      else:
        continuar = chequear_paso(tablero, turno)
        if continuar:
          pasar += 1
      if continuar:
        turno = cambiar_turno(turno)
    else:
      finalizo_antes_de_tiempo = True
      continuar = False
    if pasar > 1:
      #termina el juego y hay un ganador
      hay_ganador = True
      continuar = False
  
  f.close() # Cierra el archivo

  imprimir_tablero(tablero)
  
  print()
  if tablero_lleno(tablero) or fin_del_juego(tablero):
    marcador = contar_fichas(tablero) 
    resultado(jugadores, marcador)
  else: #Finalizo antes de tiempo (se podian realizar mas jugadas)
    print('El juego podria continuar y es turno de las ' +
          ('Blancas' if turno == 1 else 'Negras'))

main()