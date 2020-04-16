#Los 0 representan celdas vacias en el carton.
#Los 1 representan celdas ocupadas en el carton.
def carton():
    carton = (
        #Modifico el carton para dejar una fila completamente vacia y asi probar si test_filas funciona bien
        (0,0,0,0,0,0,0,0,0),
        (1,1,1,1,1,1,1,1,1),
        (0,1,0,1,1,0,1,1,1),
    )
    return carton

print(carton())