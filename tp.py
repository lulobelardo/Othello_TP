#crear_tablero: None -> List(List(Int))
#Con esta funcion podemos retornar el tablero inicial
def crear_tablero():
  return [[0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,1,2,0,0,0],
          [0,0,0,2,1,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0]]


#direccion (fila,columna) -1 0 1
#modificar_tablero: 
#Toma el tablero, la tupla con la jugada, el 1\0 depende quien juegue y la direccion a chequear (8 posibles)
def modificar_tablero(tablero,jugada,turno,direccion):
  cambio = 0  #Lugar a cambiar es vacio
  condicion = True 
  suma = 1 #Contador que nos permetira mover segun corresponda
  while condicion: #El ciclo seguira mientras la condicion sea True 
    if jugada[0]+suma*direccion[0] not in range(8) or jugada[1]+suma*direccion[1] not in range(8): #Caso que la jugada se salga del tablero
      condicion = False
    elif suma == 1:
      if tablero[jugada[0]+suma*direccion[0]][jugada[1]+suma*direccion[1]] in (0,turno): #Caso que haya una ficha del mismo color
        condicion = False
    elif tablero[jugada[0]+suma*direccion[0]][jugada[1]+suma*direccion[1]] == 0: #Caso que no haya ninguna ficha
      condicion = False
    elif tablero[jugada[0]+suma*direccion[0]][jugada[1]+suma*direccion[1]] == turno: #Caso que 
      cambio = suma
      condicion = False
    #elif la ficha es del otro turno
    suma+=1
  
  for lugar in range(1,cambio): #Nos permite cambiar el color de las fichas encerradas
    tablero[jugada[0]+lugar*direccion[0]][jugada[1]+lugar*direccion[1]] = turno

def realizar_jugada(tablero, jugada, turno):
  if tablero[jugada[0]][jugada[1]] in (1,2):
    return False
  if jugada[0] not in range(8) or jugada[1] not in range(8):
    return False
  
  tablero2 = tablero[:]

  tablero[jugada[0]][jugada[1]] = turno

  #derecha
  modificar_tablero(tablero,jugada,turno,(0,1))
  #izquierda
  modificar_tablero(tablero,jugada,turno,(0,-1))
  #arriba
  modificar_tablero(tablero,jugada,turno,(-1,0))
  #abajo
  modificar_tablero(tablero,jugada,turno,(1,0))
  #diagonal abajo izquierda
  modificar_tablero(tablero,jugada,turno,(1,-1))
  #diagonal abajo derecha
  modificar_tablero(tablero,jugada,turno,(1,1))
  #diagonal arriba derecha
  modificar_tablero(tablero,jugada,turno,(-1,1))
  #diagonal arriba izquierda
  modificar_tablero(tablero,jugada,turno,(-1,-1))

  print(tablero)

def main():
  tablero = crear_tablero() #Se crea el tablero inicial
  f = open('datos.txt','r') #Se abre el archivo para lectura
  
  jugador1 = f.readline()[:-1].split(',') #Se almacena en jugador1 una lista con el nombre y con el color de ficha
  jugador2 = f.readline()[:-1].split(',') #Se almacena en jugador2 una lista con el nombre y con el color de ficha
  inicial = f.readline()[:-1] #Se almacena en inicial la letra del color de la ficha que inicia el juego (B\N)
  
  letras = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7} #Diccionario de columnas con su representacion numerica
  
  turno = (1 if inicial == 'B' else 2) #'B':1 ,'N':2

  codigo = True

  for line in f:
    jugada = (int(line[1])-1, letras[line[0]]) #Se pasa la jugada a una tupla numerica (x,y)
    #print(tablero) 
    codigo = realizar_jugada(tablero, jugada, turno)
    #turno = cambiar_turno(turno)\
    break

  f.close()

main()