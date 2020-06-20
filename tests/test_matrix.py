from src.bingo import carton
from src.bingo import validar_matrix

def test_matrix():
    mi_carton = (
       (0,0,0,0,0,0,0,0,1),
       (0,0,0,0,0,0,1,0,0),
       (0,0,0,0,0,0,0,0,1),
   )
    assert validar_matrix(mi_carton) == True
    mi_carton_falso = (
       (0,0,0,0,0,0,0,0,1),
       (0,0,0,0,0,0,1,0),
       (0,0,0,0,0,0,0,0,1),
   )
    assert validar_matrix(mi_carton_falso) == False