import math
import random
from bingo import carton
from bingo import validar_quince_numeros
from bingo import validar_no_menor_a_quince
from bingo import validar_no_mayor_a_quince
from bingo import validar_no_columnas_vacias
from bingo import validar_no_filas_vacias
from bingo import validar_uno_a_noventa
from bingo import validar_avance_filas
from bingo import validar_avance_columnas
from bingo import validar_no_repetidos
from bingo import validar_5_filas_ocupadas
from bingo import validar_matrix
from bingo import validar_columnas_ocupadas
from bingo import validar_3_columnas
from bingo import validar_dosvacias_consecutivas
from bingo import validar_dosocupadas_consecutivas

# Algorimo adaptado de:
# https://github.com/vicmagv/bingo-card-generator

def intentoCarton():
    contador = 0
    carton = (
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0]
    )
    numerosCarton = 0

    while numerosCarton < 15:
        contador += 1
        if contador == 50:
            return intentoCarton()
        numero = random.randint(1, 90)

        columna = math.floor(numero / 10)
        if columna == 9:
            columna = 8
        huecos = 0
        for i in range(0,3): 
            if carton[columna][i] == 0:
                huecos += 1
            if carton[columna][i] == numero:
                huecos = 0
                break
        if huecos < 2:
            continue

        fila = 0
        for j in range(0,3):
            huecos = 0
            for i in range(0,9):
                if carton[i][fila] == 0:
                    huecos += 1

            if huecos < 5 or carton[columna][fila] != 0:
                fila += 1
            else:
                break
        if fila == 3:
            continue

        carton[columna][fila] = numero
        numerosCarton += 1
        contador = 0
    for x in range(0,9):
        huecos = 0
        for y in range (0,3):
            if carton[x][y] == 0:
                huecos += 1
        if huecos == 3:
            return intentoCarton()

    return carton

def imprimirCarton(carton):
    #print("\n")
    #for columna in range(0,3):
        #for fila in range(0,9):
       #     #print(" %2d ",carton[fila][columna])
      #      print(carton[fila][columna], end = ' ')
     #   print("\n")
    #print("\n")
    print("\n")
    for fila in range(0,3):
        for columna in range(0,9):
            #print(" %2d ",carton[fila][columna])
            print(carton[fila][columna], end = ' ')
        print("\n")
    print("\n")

#Se encarga de transformar el carton que pasa intentoCarton a uno que pueda interpretarse por las funciones que ya creamos antes
def transformar_carton(carton):
    carton_interpretable= (
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    )
    for x in range (0,3):
        for y in range (0,9):
            carton_interpretable[x][y] = carton[y][x]
    return carton_interpretable

#Corre todos los tests en el carton que se le pase y devuelve True si pasa todos ellos de forma satisfactoria
def tests_carton(carton_transformado):
    if (validar_quince_numeros(carton_transformado) != True)
    or ((validar_no_menor_a_quince(carton_transformado) != True)
    or (validar_no_mayor_a_quince(carton_transformado) != True)
    or (validar_no_columnas_vacias(carton_transformado) != True)
    or (validar_no_filas_vacias(carton_transformado) != True)
    or (validar_uno_a_noventa(carton_transformado) != True)
    or (validar_avance_filas(carton_transformado) != True)
    or (validar_avance_columnas(carton_transformado) != True)
    or (validar_no_repetidos(carton_transformado) != True)
    or (validar_5_filas_ocupadas(carton_transformado) != True)
    or (validar_matrix(carton_transformado) != True)
    or (validar_columnas_ocupadas(carton_transformado) != True)
    or (validar_3_columnas(carton_transformado) != True)
    or (validar_dosvacias_consecutivas(carton_transformado) != True)
    or (validar_dosocupadas_consecutivas(carton_transformado) != True):
        return False
    else:
        return True

#Transforma cada carton generado para luego testearlo, hasta encontrar uno que cumpla con todos los criterios y devolverlo
def carton_definitivo():
    #contador = 0
    while True:
        #contador += 1
        #print(contador)
        carton_original = intentoCarton()
        carton_transformado = transformar_carton(carton_original)
        if tests_carton(carton_transformado) == True:
            break
    return carton_transformado

def main():
    imprimirCarton(carton_definitivo())

if __name__ == '__main__':
    main()
