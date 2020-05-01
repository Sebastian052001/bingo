#Los 0 representan celdas vacias en el carton.
#Los 1 representan celdas ocupadas en el carton.
def carton():
    carton = (
        #Modifico el carton para dejar una fila completamente vacia y asi probar si test_filas funciona bien
        (0,1,0,1,0,1,1,0,1),
        (1,0,1,1,1,0,1,1,0),
        (0,1,0,0,1,0,0,1,1),
    )
    return carton

def validar_quince_numeros(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
                celdas_vacias =  celdas_vacias + 1
    return celdas_vacias == 12

print(carton())