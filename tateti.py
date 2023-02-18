# Import random 
import random

# Funcion que imprime el tablero bonito
def pintar_tablero(matriz):
    print('|' + str(matriz[0][0]) + '|' + str(matriz[0][1]) + '|' + str(matriz[0][2]) + '|')
    print('|' + str(matriz[1][0]) + '|' + str(matriz[1][1]) + '|' + str(matriz[1][2]) + '|')
    print('|' + str(matriz[2][0]) + '|' + str(matriz[2][1]) + '|' + str(matriz[2][2]) + '|')

# Bienvenida al jugar
print("Bienvenido TA-TE-TI -  Carlos Cifuentes")

# Menu del juego
while True:
    try:
       print("Para jugar ingrese la opcion 1 para jugar o 2 para terminar el juego")
       opcion = int(input("Opcion: "))
    except:
        print("El valor ingresado no es numerico!")
    else:
        if opcion == 1:
            print("Empezemos a jugar")
            l = '_' # Tablero libre con giones iniciales
            tablero = [
                [l,l,l],
                [l,l,l],
                [l,l,l]
            ]
            pintar_tablero(tablero)
            while True:
                estado = input("Ingrese el simbolo a jugar (X/O): ")
                if 'X' == estado or estado.upper() == 'X':
                    print("Las X empiezan adelante")
                    ocupacion = 0
                    while True:
                        print("Recuerda que es tipo matriz y empieza de 0")
                        entrada = input('Ingrese la coordenada en formato fila-columna: Ejemplo: 0-3 -----> ')
                        
                        coordenadas = entrada.split('-')
                        f = int(coordenadas[0])
                        c = int(coordenadas[1])
                        if f >= 0 and f <= 2 and c >=0 and c <=2 and tablero[f][c] != 'O':
                            tablero[f][c] = 'X'
                            num1 = random.randint(0,2)
                            num2 = random.randint(0,2)
                            if tablero[num1][num2] != 'X' and tablero[num1][num2] == '_':
                                tablero[num1][num2] = 'O'
                                ocupacion += 2
                                pintar_tablero(tablero)
                            elif tablero[num2][num1] != 'X' and tablero[num2][num1] == '_':
                                tablero[num2][num1] = 'O'
                                ocupacion += 2
                                pintar_tablero(tablero)
                            elif tablero[num1][num1] != 'X' and tablero[num1][num1] == '_':
                                tablero[num1][num1] = 'O'
                                ocupacion += 2
                                pintar_tablero(tablero)
                            elif tablero[num2][num2] != 'X' and tablero[num2][num2] == '_':
                                tablero[num2][num2] = 'O'
                                ocupacion += 2
                                pintar_tablero(tablero)
                            else:
                                num1 = random.randint(0,2)
                                num2 = random.randint(0,2)
                                if tablero[num1][num2] != 'X' and tablero[num1][num2] == '_':
                                    tablero[num1][num2] = 'O'
                                    ocupacion += 2
                                    pintar_tablero(tablero)  

                            # Validacion posibles ganadas son 8 opciones para ganar
                            if (tablero[0][0] == 'X' and tablero[0][1] == 'X' and tablero[0][2] == 'X') or (tablero[0][0] == 'O' and tablero[0][1] == 'O' and tablero[0][2] == 'O'):
                                letra = tablero[0][0]
                                if letra == 'X':
                                    pintar_tablero(tablero)
                                    print("Ganaste!!!")
                                    break
                                else:
                                    pintar_tablero(tablero)
                                    print("Perdiste")
                                    break
                            elif (tablero[1][0] == 'X' and tablero[1][1] == 'X' and tablero[1][2] == 'X') or (tablero[1][0] == 'O' and tablero[1][1] == 'O' and tablero[1][2] == 'O'):
                                letra = tablero[1][0]
                                if letra == 'X':
                                    pintar_tablero(tablero)
                                    print("Ganaste!!!")
                                    break
                                else:
                                    pintar_tablero(tablero)
                                    print("Perdiste")
                                    break
                            elif (tablero[2][0] == 'X' and tablero[2][1] == 'X' and tablero[2][2] == 'X') or (tablero[2][0] == 'O' and tablero[2][1] == 'O' and tablero[2][2] == 'O'):
                                letra = tablero[2][0]
                                if letra == 'X':
                                    pintar_tablero(tablero)
                                    print("Ganaste!!!")
                                    break
                                else:
                                    pintar_tablero(tablero)
                                    print("Perdiste")
                                    break
                            elif (tablero[0][0] == 'X' and tablero[1][0] == 'X' and tablero[2][0] == 'X') or (tablero[0][0] == 'O' and tablero[1][0] == 'O' and tablero[2][0] == 'O'):
                                letra = tablero[0][0]
                                if letra == 'X':
                                    pintar_tablero(tablero)
                                    print("Ganaste!!!")
                                    break
                                else:
                                    pintar_tablero(tablero)
                                    print("Perdiste")
                                    break
                            elif (tablero[0][1] == 'X' and tablero[1][1] == 'X' and tablero[2][1] == 'X') or (tablero[0][1] == 'O' and tablero[1][1] == 'O' and tablero[2][1] == 'O'):
                                letra = tablero[0][0]
                                if letra == 'X':
                                    pintar_tablero(tablero)
                                    print("Ganaste!!!")
                                    break
                                else:
                                    pintar_tablero(tablero)
                                    print("Perdiste")
                                    break
                            elif (tablero[0][2] == 'X' and tablero[1][2] == 'X' and tablero[2][2] == 'X') or (tablero[0][2] == 'O' and tablero[1][2] == 'O' and tablero[2][2] == 'O'):
                                letra = tablero[0][0]
                                if letra == 'X':
                                    pintar_tablero(tablero)
                                    print("Ganaste!!!")
                                    break
                                else:
                                    pintar_tablero(tablero)
                                    print("Perdiste")
                                    break
                            elif (tablero[0][0] == 'X' and tablero[1][1] == 'X' and tablero[2][2] == 'X') or (tablero[0][0] == 'O' and tablero[1][1] == 'O' and tablero[2][2] == 'O'):
                                letra = tablero[0][0]
                                if letra == 'X':
                                    pintar_tablero(tablero)
                                    print("Ganaste!!!")
                                    break
                                else:
                                    pintar_tablero(tablero)
                                    print("Perdiste")
                                    break
                            elif (tablero[0][2] == 'X' and tablero[1][1] == 'X' and tablero[2][0] == 'X') or (tablero[0][2] == 'O' and tablero[1][1] == 'O' and tablero[2][0] == 'O'):
                                letra = tablero[0][0]
                                if letra == 'X':
                                    pintar_tablero(tablero)
                                    print("Ganaste!!!")
                                    break
                                else:
                                    pintar_tablero(tablero)
                                    print("Perdiste")
                                    break
                            
                            # Validacion numero de jugadas
                            if ocupacion == 8:
                                pintar_tablero(tablero)
                                print("Empate")
                                break

                        else:
                            if tablero[f][c] == 'O' or tablero[f][c] == 'X':
                                print("La posicion ingresada ya se encuntra ocupada")
                            else:
                                print("Coordenadas fuera del tablero")
                    break
                elif 'O' == estado or estado.upper() == 'O':
                    print("Comienzan las X")
                    ocupacion = 0
                    while True:
                         num1 = random.randint(0,2)
                         num2 = random.randint(0,2)
                         if tablero[num1][num2] != 'O' and tablero[num1][num2] == '_':
                             tablero[num1][num2] = 'X'
                             ocupacion += 1
                             pintar_tablero(tablero)
                         elif tablero[num2][num1] != 'O' and tablero[num2][num1] == '_':
                             tablero[num2][num1] = 'X'
                             ocupacion += 1
                             pintar_tablero(tablero)
                         elif tablero[num1][num1] != 'O' and tablero[num1][num1] == '_':
                             tablero[num1][num1] = 'X'
                             ocupacion += 1
                             pintar_tablero(tablero)
                         elif tablero[num2][num2] != 'O' and tablero[num2][num2] == '_':
                             tablero[num2][num2] = 'X'
                             ocupacion += 1
                             pintar_tablero(tablero)
                         else:
                             num1 = random.randint(0,2)
                             num2 = random.randint(0,2)
                             if tablero[num1][num2] != 'O' and tablero[num1][num2] == '_':
                                 tablero[num1][num2] = 'X'
                                 ocupacion += 1
                                 pintar_tablero(tablero)
                             elif tablero[num2][num1] != 'O' and tablero[num2][num1] == '_':
                                 tablero[num2][num1] = 'X'
                                 ocupacion += 1
                                 pintar_tablero(tablero)
                             elif tablero[num1][num1] != 'O' and tablero[num1][num1] == '_':
                                 tablero[num1][num1] = 'X'
                                 ocupacion += 1
                                 pintar_tablero(tablero)
                             elif tablero[num2][num2] != 'O' and tablero[num2][num2] == '_':
                                 tablero[num2][num2] = 'X'
                                 ocupacion += 1
                                 pintar_tablero(tablero)

                         # Validacion posibles ganadas son 8 opciones para ganar
                         if (tablero[0][0] == 'X' and tablero[0][1] == 'X' and tablero[0][2] == 'X') or (tablero[0][0] == 'O' and tablero[0][1] == 'O' and tablero[0][2] == 'O'):
                             letra = tablero[0][0]
                             if letra == 'O':
                                 pintar_tablero(tablero)
                                 print("Ganaste!!!")
                                 break
                             else:
                                 pintar_tablero(tablero)
                                 print("Perdiste")
                                 break
                         elif (tablero[1][0] == 'X' and tablero[1][1] == 'X' and tablero[1][2] == 'X') or (tablero[1][0] == 'O' and tablero[1][1] == 'O' and tablero[1][2] == 'O'):
                             letra = tablero[1][0]
                             if letra == 'O':
                                 pintar_tablero(tablero)
                                 print("Ganaste!!!")
                                 break
                             else:
                                 pintar_tablero(tablero)
                                 print("Perdiste")
                                 break
                         elif (tablero[2][0] == 'X' and tablero[2][1] == 'X' and tablero[2][2] == 'X') or (tablero[2][0] == 'O' and tablero[2][1] == 'O' and tablero[2][2] == 'O'):
                             letra = tablero[2][0]
                             if letra == 'O':
                                 pintar_tablero(tablero)
                                 print("Ganaste!!!")
                                 break
                             else:
                                 pintar_tablero(tablero)
                                 print("Perdiste")
                                 break
                         elif (tablero[0][0] == 'X' and tablero[1][0] == 'X' and tablero[2][0] == 'X') or (tablero[0][0] == 'O' and tablero[1][0] == 'O' and tablero[2][0] == 'O'):
                             letra = tablero[0][0]
                             if letra == 'O':
                                 pintar_tablero(tablero)
                                 print("Ganaste!!!")
                                 break
                             else:
                                 pintar_tablero(tablero)
                                 print("Perdiste")
                                 break
                         elif (tablero[0][1] == 'X' and tablero[1][1] == 'X' and tablero[2][1] == 'X') or (tablero[0][1] == 'O' and tablero[1][1] == 'O' and tablero[2][1] == 'O'):
                             letra = tablero[0][1]
                             if letra == 'O':
                                 pintar_tablero(tablero)
                                 print("Ganaste!!!")
                                 break
                             else:
                                 pintar_tablero(tablero)
                                 print("Perdiste")
                                 break
                         elif (tablero[0][2] == 'X' and tablero[1][2] == 'X' and tablero[2][2] == 'X') or (tablero[0][2] == 'O' and tablero[1][2] == 'O' and tablero[2][2] == 'O'):
                             letra = tablero[0][2]
                             if letra == 'O':
                                 pintar_tablero(tablero)
                                 print("Ganaste!!!")
                                 break
                             else:
                                 pintar_tablero(tablero)
                                 print("Perdiste")
                                 break
                         elif (tablero[0][0] == 'X' and tablero[1][1] == 'X' and tablero[2][2] == 'X') or (tablero[0][0] == 'O' and tablero[1][1] == 'O' and tablero[2][2] == 'O'):
                             letra = tablero[0][0]
                             if letra == 'O':
                                 pintar_tablero(tablero)
                                 print("Ganaste!!!")
                                 break
                             else:
                                 pintar_tablero(tablero)
                                 print("Perdiste")
                                 break
                         elif (tablero[0][2] == 'X' and tablero[1][1] == 'X' and tablero[2][0] == 'X') or (tablero[0][2] == 'O' and tablero[1][1] == 'O' and tablero[2][0] == 'O'):
                             letra = tablero[0][2]
                             if letra == 'O':
                                 pintar_tablero(tablero)
                                 print("Ganaste!!!")
                                 break
                             else:
                                 pintar_tablero(tablero)
                                 print("Perdiste")
                                 break

                         while True:
                             entrada = input('Ingrese la coordenada en formato fila-columna: ')
                             coordenadas = entrada.split('-')
                             f = int(coordenadas[0])
                             c = int(coordenadas[1])
                             if f >= 0 and f <= 2 and c >=0 and c <=2 and tablero[f][c] != 'X' and tablero[f][c] == '_':
                                 tablero[f][c] = 'O'
                                 ocupacion += 1
                                 break
                             else:
                                 if tablero[f][c] == 'O' or tablero[f][c] == 'X':
                                     print("La posicion ingresada ya se encuntra ocupada")
                                 else:
                                     print("Coordenadas fuera del tablero")
                    
                         # Validacion posibles ganadas son 8 opciones para ganar
                         if (tablero[0][0] == 'X' and tablero[0][1] == 'X' and tablero[0][2] == 'X') or (tablero[0][0] == 'O' and tablero[0][1] == 'O' and tablero[0][2] == 'O'):
                             letra = tablero[0][0]
                             if letra == 'O':
                                 pintar_tablero(tablero)
                                 print("Ganaste!!!")
                                 break
                             else:
                                 pintar_tablero(tablero)
                                 print("Perdiste")
                                 break
                         elif (tablero[1][0] == 'X' and tablero[1][1] == 'X' and tablero[1][2] == 'X') or (tablero[1][0] == 'O' and tablero[1][1] == 'O' and tablero[1][2] == 'O'):
                             letra = tablero[1][0]
                             if letra == 'O':
                                 pintar_tablero(tablero)
                                 print("Ganaste!!!")
                                 break
                             else:
                                 pintar_tablero(tablero)
                                 print("Perdiste")
                                 break
                         elif (tablero[2][0] == 'X' and tablero[2][1] == 'X' and tablero[2][2] == 'X') or (tablero[2][0] == 'O' and tablero[2][1] == 'O' and tablero[2][2] == 'O'):
                             letra = tablero[2][0]
                             if letra == 'O':
                                 pintar_tablero(tablero)
                                 print("Ganaste!!!")
                                 break
                             else:
                                 pintar_tablero(tablero)
                                 print("Perdiste")
                                 break
                         elif (tablero[0][0] == 'X' and tablero[1][0] == 'X' and tablero[2][0] == 'X') or (tablero[0][0] == 'O' and tablero[1][0] == 'O' and tablero[2][0] == 'O'):
                             letra = tablero[0][0]
                             if letra == 'O':
                                 pintar_tablero(tablero)
                                 print("Ganaste!!!")
                                 break
                             else:
                                 pintar_tablero(tablero)
                                 print("Perdiste")
                                 break
                         elif (tablero[0][1] == 'X' and tablero[1][1] == 'X' and tablero[2][1] == 'X') or (tablero[0][1] == 'O' and tablero[1][1] == 'O' and tablero[2][1] == 'O'):
                             letra = tablero[0][1]
                             if letra == 'O':
                                 pintar_tablero(tablero)
                                 print("Ganaste!!!")
                                 break
                             else:
                                 pintar_tablero(tablero)
                                 print("Perdiste")
                                 break
                         elif (tablero[0][2] == 'X' and tablero[1][2] == 'X' and tablero[2][2] == 'X') or (tablero[0][2] == 'O' and tablero[1][2] == 'O' and tablero[2][2] == 'O'):
                             letra = tablero[0][2]
                             if letra == 'O':
                                 pintar_tablero(tablero)
                                 print("Ganaste!!!")
                                 break
                             else:
                                 pintar_tablero(tablero)
                                 print("Perdiste")
                                 break
                         elif (tablero[0][0] == 'X' and tablero[1][1] == 'X' and tablero[2][2] == 'X') or (tablero[0][0] == 'O' and tablero[1][1] == 'O' and tablero[2][2] == 'O'):
                             letra = tablero[0][0]
                             if letra == 'O':
                                 pintar_tablero(tablero)
                                 print("Ganaste!!!")
                                 break
                             else:
                                 pintar_tablero(tablero)
                                 print("Perdiste")
                                 break
                         elif (tablero[0][2] == 'X' and tablero[1][1] == 'X' and tablero[2][0] == 'X') or (tablero[0][2] == 'O' and tablero[1][1] == 'O' and tablero[2][0] == 'O'):
                             letra = tablero[0][2]
                             if letra == 'O':
                                 pintar_tablero(tablero)
                                 print("Ganaste!!!")
                                 break
                             else:
                                 pintar_tablero(tablero)
                                 print("Perdiste")
                                 break
                        
                        # Validacion numero de jugadas
                         if ocupacion == 8:
                             pintar_tablero(tablero)
                             print("Empate")
                             break
                    break
                else:
                    print("La opcion ingresada no es valida!!")
                    continue
        elif opcion == 2:
            print("Gracias por jugar TA-TE-TI")
            break