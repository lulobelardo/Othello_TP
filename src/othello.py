import os # Para cambiar el path según el S.O, y verificar validez del path

# crear_tablero: None -> Tablero
# Retorna el tablero inicial
'''
Tablero := List(List(Int))
0 := VACÍO
1 := B (Blancas)
2 := N (Negras)
'''
def crear_tablero() -> list:
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
Crea una matriz nueva, y luego copia -sin referenciar- cada fila del
tablero original en copia_tablero, así modificar uno no modifica el otro.
'''
def copiar_tablero(tablero: list) -> list:
  copia_tablero = [[], [], [], [], [], [], [], []]
  for indice, fila in enumerate(tablero):
    copia_tablero[indice] = fila[:] # [:] para perder referencia
  return copia_tablero

# chequear_paso: Tablero, Int -> Bool
# Retorna True si es válido que el jugador 'pase', caso contrario retorna False
'''
Toma como parámetros el tablero y de quién es el turno.
Para ver si pasar es válido, la función chequea si efectivamente ninguno de los
64 movimientos posibles es válido, caso en el que 'pasar' es correcto y retorna
True.
Si tan solo 1 movimiento es válido, entonces 'pasar' es incorrecto, termina de
hacer chequeos y retorna False.
'''
def chequear_paso(tablero: list, turno: int) -> bool:
  # Para no modificar el tablero original, trabaja sobre una copia
  copia_tablero = copiar_tablero(tablero)

  # Recorre o todo el tablero o hasta que encuentre un movimiento válido
  continuar = True
  fila = 0
  while fila < 8 and continuar:
    columna = 0
    while columna < 8 and continuar:
      continuar = not realizar_jugada(copia_tablero, (fila, columna), turno)
      columna += 1
    fila += 1
  return continuar

# modificar_tablero: Tablero, (Int, Int), Int, (Int, Int) -> None
# Modifica según la dirección indicada los valores del tablero correspondientes
'''
Toma como parámetros el tablero, la posición jugada (VÁLIDA), de quién es el
turno y la dirección que quiere modificar (8 posibles).
La función hace el movimiento COMPLETO en una dirección indicada, es decir,
voltea todas las fichas correspondientes en una dirección siempre y cuando haya
fichas que voltear.
El parámetro 'dirección' es una tupla de dos números que pueden ser -1, 0 y 1.
Los mismos reflejan la dirección fila/columna en la que se está desplazando
respectivamente. La dirección (0, 0) no existe.
'''
def modificar_tablero(tablero: list, jugada: tuple, turno: int,
                      direccion: tuple) -> None:
  # Asignaciones
  j_fila = jugada[0] # jugada_fila
  j_colum = jugada[1] # jugada_columna
  vert = direccion[0] # Vertical: variación en las filas
  horiz = direccion[1] # Horizontal: variación en las columnas

  delta_final = 0 # Representa la cantidad final de fichas a voltear
  delta = 1 # Contador momentáneo/hipotético de fichas a cambiar

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
    # Desplaza delta para analizar la siguiente posición
    delta += 1
  
  # Cambia el color de las fichas encerradas (delta_final lugares)
  for lugar in range(1, delta_final):
    tablero[j_fila + lugar * vert][j_colum + lugar * horiz] = turno

# realizar_jugada: Tablero, (Int, Int), Int -> Bool
# Si la jugada es válida, retorna True y la realiza, sino, retorna False
'''
Toma como parámetros el tablero, la jugada y el turno.
Si la jugada es inválida, retorna False y no modifica el tablero,
si en un principio la jugada es válida, entonces modifica el tablero según
corresponda en todas las direcciones, y si al hacerlo el tablero se modificó,
entonces la jugada era efectivamente válida, la realiza y retorna True. Por
otro lado, si el tablero NO se modificó, entonces la jugada era inválida, por
lo que retorna False.
'''
def realizar_jugada(tablero: list, jugada: tuple, turno: int) -> bool:
  # Caso jugada fuera de rango
  if jugada[0] not in range(8) or jugada[1] not in range(8):
    return False
  # Caso posición ocupada por otra ficha
  if tablero[jugada[0]][jugada[1]] in (1, 2):
    return False

  copia_tablero = copiar_tablero(tablero) # Copia a comparar luego

  # Modifica (o no) el tablero en todas las direcciones
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
  tablero original no afecta. Por otro lado, si se modificó, ya no hace
  falta que se vuelva a modificar, por lo que solo queda poner la ficha.
  '''
  if tablero == copia_tablero: # Si son iguales, la jugada es inválida
    return False

  tablero[jugada[0]][jugada[1]] = turno # Coloco la ficha
  return True

# cambiar_turno: Int -> Int
# Cambia el turno, si era del 1 ahora es del 2, y viceversa
def cambiar_turno(turno: int) -> int:
  return (2 if turno == 1 else 1)

# imprimir_tablero: Tablero -> None
# Imprime el tablero
def imprimir_tablero(tablero: list) -> None:
  print()
  print('    A B C D E F G H')
  print('    ---------------')
  for i, fila in enumerate(tablero):
    print(i + 1, end = ' | ')
    for valor in fila:
      if valor == 0:
        print('·', end = ' ') # Alternativas ' ' '-'
      elif valor == 1:
        print('•', end = ' ') # Alternativas 'B'
      elif valor == 2:
        print('○', end = ' ') # Alternativas 'N'
    print('|', i + 1)
  print('    ---------------')
  print('    A B C D E F G H')
  print()

# contar_fichas: Tablero -> (Int, Int)
'''
Toma el tablero (lleno o no) y retorna una tupla de números con la cantidad de
fichas de cada jugador (color) tal que (blancas, negras).
'''
def contar_fichas(tablero: list) -> tuple:
  blancas = 0 # Contador fichas blancas
  negras = 0 # Contador fichas negras

  # Recorre cada posición
  for fila in tablero:
    for ficha in fila:
      if ficha == 1: # Es blanca
        blancas += 1
      elif ficha == 2: # Es negra
        negras += 1
  return (blancas, negras)

# resultado: Dict, (Int, Int) -> None
# Muestra en pantalla el ganador según el puntaje obtenido
'''
Toma un diccionario que contiene ambos jugadores, tal que su clave es su color
('B' o 'N') y el valor es su nombre; y una tupla de enteros que contiene los
puntos del blanco y negro respectivamente.
Imprime en pantalla los puntos de cada jugador y el resultado del juego
(empate, ganan blancas o ganan negras).
'''
def resultado(jugadores: dict, marcador: tuple) -> None:
  blancas = marcador[0] # Asigna la cantidad de fichas blancas
  negras = marcador[1]  # Asigna la cantidad de fichas negras
  print('Fichas Blancas (' + jugadores['B'] + '): ' + str(blancas))
  print('Fichas Negras (' + jugadores['N'] + '): ' + str(negras))
  print() # Estética
  if blancas > negras: # Caso que ganen el jugador con fichas blancas
    print('Ganan Blancas (' + jugadores['B'] + ').')
  elif negras > blancas: # Caso que ganen el jugador con fichas negras
    print('Ganan Negras (' + jugadores['N'] + ').')
  else: # Caso que haya un empate
    print('Empate')
  print()

# convertir_fila: String -> Int
# Toma un número como string y retorna el número como Int - 1
'''
Toma como parámetro una string de un caracter (representa la fila). Este
debería ser un dígito.
Si es un entero, retorna el anterior a dicho valor, pues traduce el conteo
'Humano' (comienza por 1) al informático (comienza por 0). Por otra parte, si
es una letra o cualquier otro caracter, retorna -1 como aviso de que es erróneo
el dato (si toma '0' también es erróneo, por lo que no genera problema).
Si toma '9', el movimiento igualmente será fuera de rango, por lo que no afecta
'''
def convertir_fila(caracter: str) -> bool:
  try:
    return int(caracter) - 1
  except ValueError:
    return -1 # El programa sólo verifica que el dato es erróneo luego

# convertir_fila: String -> Int
# Toma una letra como string y retorna el número de columna correspondiente
'''
Toma como parámetro una string de un caracter (representa la columna). Este
debería ser una letra en el rango A-H.
Retorna el valor asociado de cada letra al número de columna.
Si el dato es erróneo, retorna -1 como aviso del fallo.
'''
def convertir_columna(caracter: str) -> bool:
  # Diccionario de columnas con su representación numérica
  letras = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
  try:
    return letras[caracter]
  except KeyError:
    return -1

# fin_del_juego: Tablero -> Bool
'''
Toma un tablero.
Si no se pueden realizar jugadas retorna True, caso contrario retorna False.
Si ambos pueden pasar con el tablero parámetro, entonces el juego termina.
'''
def fin_del_juego(tablero: list) -> bool:
  if chequear_paso(tablero, 1) and chequear_paso(tablero, 2):
    return True
  else:
    return False

# chequear_y_corregir_jugador: List(String) -> List(String)
'''
Toma una lista de string, que si esta bien ingresada consta de dos elementos:
el primero un nombre y el segundo es el color de la ficha.
Retorna lista vacía si el largo de la lista es distinto de 2 o si el segundo
elemento no correspone a un color de ficha. Si los datos
son correctos devuelve la lista original, despreciando los ' ' y el '\n' del
color (lo considera correcto igualmente).
Se considera que el nombre siempre es correcto tal como es.
'''
def chequear_y_corregir_jugador(jugador: list) -> list:
  if len(jugador) != 2:
    return []
  jugador[1] = jugador[1].strip()
  if jugador[1] not in ('N', 'B'):
    return []
  return jugador

# main: String -> None
# El juego de Othello como tal, toma un path de una partida y la 'juega'
# Retorna 0 si la partida comenzó, y otro int si hubo algún error previo
def main(path: str) -> None:
  # Apertura del archivo
  f = None
  if os.path.isfile(path): # Si existe el archivo con ese path
    f = open(path, 'r') # Se abre el archivo para lectura
  else:
    print('\nEl path es incorrecto o el archivo es inexistente.\n')
    return None # Finaliza con 'error' el juego
  
  # Guarda cada jugador en una lista con el nombre y con el color de ficha
  jugador1 = f.readline().split(',')
  jugador1 = chequear_y_corregir_jugador(jugador1)

  jugador2 = f.readline().split(',')
  jugador2 = chequear_y_corregir_jugador(jugador2)

  # Chequea la validez de los datos obtenidos
  if not jugador1 or not jugador2:
    print('\nAlguno de los jugadores esta mal ingresado.\n')
    return None # Finaliza con 'error' el juego
  if jugador1[1] == jugador2[1]:
    print('\nAmbos jugadores tienen el mismo color asignado.\n')
    return None # Finaliza con 'error' el juego

  '''
  Guarda los jugadores en un diccionario cuya clave es el color de la ficha
  y el valor es el nombre del jugador. De la forma:
  {B/N: nombre del jugador1, N/B: nombre del jugador2}.
  '''
  jugadores = {jugador1[1]: jugador1[0], jugador2[1]: jugador2[0]}

  # Asigna a inicial la letra del color de la ficha que inicia el juego (B\N)
  inicial = f.readline().strip() # (.strip() para despreciar ' ' y '\n')
  # Traslada ese valor a un número (1: B, 2: N) que indica el respectivo turno
  turno = 0
  if inicial == 'B':
    turno = 1 # 'B': 1
  elif inicial == 'N':
    turno = 2 # 'N': 2
  else: # No leyó ni N ni B
    print('\nNo esta correctamente indicado que jugador comienza.\n')
    return None # Finaliza con 'error' el juego
  
  # Asignaciones
  tablero = crear_tablero() # Crea el tablero
  pasar = 0 # Contador de veces que se 'pasa' de manera consecutiva
  continuar = True # True si el bucle continua, False si debe terminar
  fin_de_archivo = False # Indica si el archivo se leyó por completo
  pasar_incorrecto = False # Indica si se 'pasó' incorrectamente
  error_de_formato = False # Indica si hay un error de FORMATO en el archivo
  posicion_ilegal = False # Indica si la posición es fuera de rango/ilegal
  hay_lineas_extra = False # Indica si el archivo continua luego de finalizar
  line = '' # Representa cada línea del archivo

  while continuar:
    line = f.readline().replace(' ', '') # Lee línea por linea
    if line: # Mientras la jugada no sea el EOF ('', string vacío)
      # Si tiene 2 LETRAS EXACTAS, podria ser válido
      if len(line) == 3 or (len(line) == 2 and line[-1] != '\n'):
        fila = convertir_fila(line[1]) # int(line[1]) - 1
        columna = convertir_columna(line[0]) # letras[line[0]]
        jugada = (fila, columna) # Pasa la jugada a una tupla numerica (x, y)
        # Intenta realizar la jugada, y si puede la hace, sino termina el juego
        continuar = realizar_jugada(tablero, jugada, turno)
        if not continuar: # Si la jugada fue inválida, movimiento ilegal
          posicion_ilegal = True
          hay_lineas_extra = True # Por si ya había terminado el juego
        pasar = 0 # Resetea el contador de 'paso'
      elif line == '\n': # Intenta 'pasar'
        # Chequea si es válido haber 'pasado', si es válido sigue, sino termina
        continuar = chequear_paso(tablero, turno)
        if continuar: # Si pasar fue válido, aumenta el contador
          pasar += 1
        else: # Especifica porque termino antes de tiempo
          pasar_incorrecto = True
      else: # La linea tiene 1 o +2 caracteres != '\n', movimiento inválido
        error_de_formato = True
        hay_lineas_extra = True # Por si ya había terminado el juego
        continuar = False # Termina el juego
      if continuar: # Si el juego va a continuar, cambia el turno
        turno = cambiar_turno(turno)
    else: # LLegó al final del archivo
      fin_de_archivo = True
      continuar = False # Termina el juego
    if pasar > 1: # Se 'pasó' CORRECTAMENTE dos veces
      if f.readline(): # Si pasaron 2 veces, pero sigue habiendo lineas
        hay_lineas_extra = True
      continuar = False # Termina el juego

  f.close() # Cierra el archivo

  imprimir_tablero(tablero) # Imprime el tablero (hasta donde se modificó)

  if fin_del_juego(tablero):
    if hay_lineas_extra:
      print('ADVERTENCIA: El juego finalizó correctamente pero hay lineas ' +
            'de más en el archivo.\n')
    marcador = contar_fichas(tablero)
    resultado(jugadores, marcador)
  else: # Finalizó antes de tiempo (se podían realizar mas jugadas)
    if posicion_ilegal:
      print('Movimiento inválido: (' + line.strip() + ') Posición ilegal.\n')
    if pasar_incorrecto:
      print('Movimiento inválido: "Pasar" no es válido en esta posición.\n')
    if error_de_formato:
      print('Movimiento inválido: (' + line.strip() + ') Error de formato.\n')
    if fin_de_archivo:
      print('El juego está incompleto.\n')
    print('El juego podria continuar y es turno de las ' +
         ('Blancas' if turno == 1 else 'Negras') + '.\n')

# El path varía según el SO
main(('./src/' if os.name == 'posix' else '.\\src\\') + 'juego1.txt')