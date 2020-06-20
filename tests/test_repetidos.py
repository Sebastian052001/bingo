from src.bingo import carton
from src.bingo import validar_no_repetidos

def test_no_repetidos():
    mi_carton = (
       (0,0,0,0,0,0,0,0,1),
       (0,0,0,90,0,5,0,0,0),
       (0,0,0,6,0,0,0,80,75),
   )
    assert validar_no_repetidos(mi_carton) == True
    mi_carton_falso = (
       (0,90,0,0,0,0,0,0,1),
       (0,0,0,90,0,5,90,0,0),
       (0,0,0,6,0,0,0,80,75),
   )
    assert validar_no_repetidos(mi_carton_falso) == False