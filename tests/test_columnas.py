from src.bingo import carton
from src.bingo import validar_columnas_ocupadas
from src.bingo import validar_3_columnas

def test_columnas_ocupadas():
    mi_carton = (
       (0,1,1,1,0,0,0,0,1),
       (1,0,1,0,1,0,1,1,0),
       (0,0,1,1,0,1,0,0,1),
   )
    assert validar_columnas_ocupadas(mi_carton) == True
    mi_carton_falso = (
       (0,1,1,1,0,0,0,0,1),
       (1,0,1,0,0,0,1,1,0),
       (0,0,1,1,0,1,0,0,1),
   )
    assert validar_columnas_ocupadas(mi_carton_falso) == False

def test_3_columnas():
    mi_carton = (
       (0,1,0,1,1,0,1,0,1),
       (1,0,0,0,1,1,1,1,0),
       (0,0,1,1,0,1,0,1,1),
   )
    assert validar_3_columnas(mi_carton) == True
    mi_carton_falso = (
       (0,1,0,1,1,0,1,0,1),
       (1,0,0,0,1,1,1,1,0),
       (0,0,1,0,0,1,0,1,1),
   )
    assert validar_3_columnas(mi_carton_falso) == False