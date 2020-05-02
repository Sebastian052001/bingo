from src.bingo import carton
from src.bingo import validar_quince_numeros
from src.bingo import validar_no_menor_a_quince
from src.bingo import validar_no_mayor_a_quince
from src.bingo import validar_no_columnas_vacias

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
    assert validar_no_menor_a_quince(mi_carton) == True

def test_cantidad_no_mayor_a_quince():
    mi_carton = (
       (1,0,1,0,0,1,0,1,1),
       (1,1,0,1,1,0,1,0,1),
       (1,0,0,0,1,0,0,1,1),
   )
    assert validar_no_mayor_a_quince(mi_carton) == True

def test_columnas_vacias():
    mi_carton = (
       (1,1,1,1,1,1,1,1,1),
       (1,1,1,1,1,1,1,1,1),
       (1,1,1,1,1,1,1,1,1),
   )
    assert validar_no_columnas_vacias(mi_carton) == True

