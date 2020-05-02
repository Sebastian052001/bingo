#Los 0 representan celdas vacias en el carton.
#Los 1 representan celdas ocupadas en el carton.
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
def validar_no_menor_a_15(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
                celdas_vacias = celdas_vacias + 1
    return celdas_vacias <= 12

#Valida que la cantidad de celdas ocupadas en el carton no sea mayor a 15
def validar_no_mayor_a_15(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
                celdas_vacias = celdas_vacias + 1
    return celdas_vacias >= 12
    
print(carton())