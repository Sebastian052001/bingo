from src.bingo import carton
from src.bingo import validar_uno_a_noventa

def test_uno_a_noventa():
    mi_carton = (
       (0,0,0,0,0,0,0,0,1),
       (0,0,0,90,0,1,0,0,0),
       (0,0,0,0,0,0,0,0,75),
   )
    assert validar_uno_a_noventa(mi_carton) == True
    mi_carton_falso = (
       (0,0,0,0,0,0,0,0,1),
       (0,95,0,90,0,1,0,0,0),
       (0,0,0,0,0,0,120,0,75),
   )
    assert validar_uno_a_noventa(mi_carton_falso) == False