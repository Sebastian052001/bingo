import math
import random
#Los 0 representan celdas vacias en el carton.
#Los 1 representan celdas ocupadas en el carton.
#Antigua definicion de carton:
def carton():
    carton = (
        (0,1,0,1,0,1,1,0,1),
        (1,0,1,1,1,0,1,1,0),
        (0,1,0,0,1,0,0,1,1),
    )
    return carton

#Valida que haya quince celdas ocupadas en el carton
def validar_quince_numeros(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
                celdas_vacias =  celdas_vacias + 1
    return celdas_vacias == 12

#Valida que la cantidad de celdas ocupadas en el carton no sea menor a 15
def validar_no_menor_a_quince(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
                celdas_vacias = celdas_vacias + 1
    return celdas_vacias <= 12

#Valida que la cantidad de celdas ocupadas en el carton no sea mayor a 15
def validar_no_mayor_a_quince(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
                celdas_vacias = celdas_vacias + 1
    return celdas_vacias >= 12

#Valida que ninguna de las columnas del carton esten absolutamente vacias
def validar_no_columnas_vacias(carton):
    columnas_no_vacias = 0
    for x in range(0,9): 
        if carton[0][x]+carton[1][x]+carton[2][x] > 0:
            columnas_no_vacias = columnas_no_vacias + 1
    return columnas_no_vacias == 9

#Valida que ninguna de las filas del carton esten absolutamente vacias
def validar_no_filas_vacias(carton):
    filas_no_vacias = 0
    for x in range(0,3):
        celdas_ocupadas = 0
        for y in range(0,9):
            celdas_ocupadas += carton[x][y]
        if celdas_ocupadas > 0:
            filas_no_vacias = filas_no_vacias + 1
    return filas_no_vacias == 3

#Valida que los numeros del carton esten comprendidos entre 1 y 90
def validar_uno_a_noventa(carton):
    casillas_validas = 0
    for fila in range(0,3):
        for columna in range(0,9):
          celda = carton[fila][columna]
          if celda >= 0 and celda <=90:
              casillas_validas = casillas_validas + 1
    return casillas_validas == 27

#Valida que en cada fila los numeros avancen de menor a mayor
def validar_avance_filas(carton):
    bool_filas = True
    for columna in range(0,3):
        casilla_anterior = -1
        for fila in range(0,9):
            celda = carton[columna][fila]
            if celda < casilla_anterior and celda != 0:
                bool_filas = False
            if celda != 0:
                casilla_anterior = celda
    return bool_filas

#Valida que en cada columna los numeros avancen de menor a mayor
def validar_avance_columnas(carton):
    bool_filas = True
    for fila in range (0,9):
        casilla_anterior = -1
        for columna in range(0,3):
                celda = carton[columna][fila]
                if celda < casilla_anterior and celda != 0:
                    bool_filas = False
                if celda != 0:
                    casilla_anterior = celda
    return bool_filas

#Valida que no haya numeros repetidos en el mismo carton
def validar_no_repetidos(carton):
    bool_repetidos = True
    lista_elementos_carton = []
    #Creo una lista que contenga todos los elementos del carton que no sean 0
    for columna in range(0,3):
        for fila in range(0,9):
            celda = carton[columna][fila]
            if celda != 0:
                lista_elementos_carton.append(celda)
    #Si la cantidad de veces que aparece un elemento en la lista es mayor a 1, devuelve False
    for columna in range (0,3):
        for fila in range(0,9):
            celda = carton[columna][fila]
            if celda != 0:
                if lista_elementos_carton.count(celda) != 1:
                    bool_repetidos = False
    return bool_repetidos

#Valida que cada fila de un carton tenga exactamente 5 filas ocupadas
def validar_5_filas_ocupadas(carton):
    bool_valido = True
    contador = 5
    for x in range(0,3):
        if contador != 5:
            bool_valido = False
        contador = 0
        for y in range(0,9):
            if carton[x][y]!= 0:
                contador = contador + 1
    return bool_valido

#Valida que cada carton sea una matrix de 3x9
def validar_matrix(carton):
    bool_valido = True
    if len(carton) != 3:
        bool_valido = False
    else:
        for x in range(0,3):
            if len(carton[x]) != 9:
                bool_valido = False
    return bool_valido

#Valida que cada carton no tenga ninguna columna con sus tres celdas vacias
def validar_columnas_ocupadas(carton):
    bool_valido = True
    for x in range(0,9):
        if (carton[0][x] == 0) and (carton[1][x] == 0) and (carton[2][x] == 0):
            bool_valido = False
    return bool_valido

#Valida que solo existan 3 columnas con solo una celda ocupada
def validar_3_columnas(carton):
    bool_valido = True
    contadorcolumnas = 0
    for y in range (0,9):
        contador = 0
        for x in range(0,3):
            if carton[x][y] != 0:
                contador = contador + 1
        if contador == 1:
            contadorcolumnas = contadorcolumnas + 1
    if contadorcolumnas != 3:
        bool_valido = False
    return bool_valido

#Valida que en una fila no existan mas de dos celdas vacias consecutivas
def validar_dosvacias_consecutivas(carton):
    bool_valido = True
    for x in range (0,3):
        for y in range (0,7):
            if (carton[x][y] == 0) and (carton[x][y+1] == 0) and (carton[x][y+2] == 0):
                bool_valido = False
    return bool_valido

#Valida que en una fila no existan mas de dos celdas ocupadas consecutivas
def validar_dosocupadas_consecutivas(carton):
    bool_valido = True
    for x in range (0,3):
        for y in range (0,7):
            if (carton[x][y] != 0) and (carton[x][y+1] != 0) and (carton[x][y+2] != 0):
                bool_valido = False
    return bool_valido

#Se encarga de crear un carton que luego se sometera a los tests
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

#Muestra en pantalla el carton
def imprimirCarton(carton):
    print("\n")
    for fila in range(0,3):
        for columna in range(0,9):
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
def pruebas_carton(carton_transformado):
    #Por motivos que desconozco al dejar un enter por cada or en el if de abajo el programa lo toma como un error de sintaxis por lo que me veo forzado a escribir todo en la misma linea
    if (validar_quince_numeros(carton_transformado) != True) or (validar_no_menor_a_quince(carton_transformado) != True) or (validar_no_mayor_a_quince(carton_transformado) != True) or (validar_no_columnas_vacias(carton_transformado) != True) or (validar_no_filas_vacias(carton_transformado) != True) or (validar_uno_a_noventa(carton_transformado) != True) or (validar_avance_filas(carton_transformado) != True) or (validar_avance_columnas(carton_transformado) != True) or (validar_no_repetidos(carton_transformado) != True) or (validar_5_filas_ocupadas(carton_transformado) != True) or (validar_matrix(carton_transformado) != True) or (validar_columnas_ocupadas(carton_transformado) != True) or (validar_3_columnas(carton_transformado) != True) or (validar_dosvacias_consecutivas(carton_transformado) != True) or (validar_dosocupadas_consecutivas(carton_transformado) != True):
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
        if pruebas_carton(carton_transformado) == True:
            break
    return carton_transformado

def main():
    imprimirCarton(carton_definitivo())

if __name__ == '__main__':
    main()