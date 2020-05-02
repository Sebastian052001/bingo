from src.bingo import carton
from src.bingo import validar_quince_numeros
from src.bingo import validar_no_menor_a_15
from src.bingo import validar_no_mayor_a_15

def test_contar_celdas_ocupadas():
   mi_carton = (
       (1,0,1,0,0,1,0,1,1),
       (1,1,0,1,1,0,1,0,1),
       (1,0,0,0,1,0,0,1,1),
   )
   assert validar_quince_numeros(mi_carton) == True

def test_cantidad_no_menor_a_quince():
    mi_carton = (
       (1,0,1,0,0,1,0,1,1),
       (1,1,0,1,1,0,1,0,1),
       (1,0,0,0,1,0,0,1,1),
   )
   assert validar_no_menor_a_15(mi_carton) == True

def test_cantidad_no_mayor_a_quince():
    mi_carton = (
       (1,0,1,0,0,1,0,1,1),
       (1,1,0,1,1,0,1,0,1),
       (1,0,0,0,1,0,0,1,1),
   )
   assert validar_no_mayor_a_15(mi_carton) == True


#comprueba que ninguna de las columnas del carton esten absolutamente vacias
def test_columna():
    mi_carton = carton()
    for x in range(0,8): 
        assert mi_carton[0][x]+mi_carton[1][x]+mi_carton[2][x] > 0

