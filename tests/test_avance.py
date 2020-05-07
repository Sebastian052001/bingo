from src.bingo import carton
from src.bingo import validar_avance_filas

def test_avance_filas():
    mi_carton = (
       (1,0,3,0,0,15,0,25,30),
       (4,5,0,8,9,0,10,0,11),
       (9,50,65,0,70,0,80,0,0),
   )
    assert validar_avance_filas(mi_carton) == True