from src.bingo import carton
from src.bingo import validar_no_filas_vacias
from src.bingo import validar_5_filas_ocupadas
from src.bingo import validar_dosvacias_consecutivas
from src.bingo import validar_dosocupadas_consecutivas

def test_filas_vacias():
    mi_carton = (
       (0,0,0,0,0,0,0,0,1),
       (0,0,0,0,0,0,1,0,0),
       (0,0,0,0,0,0,0,0,1),
   )
    assert validar_no_filas_vacias(mi_carton) == True

def test_5_filas_ocupadas():
    mi_carton = (
       (1,0,1,0,1,0,1,1,0),
       (1,0,1,0,1,0,1,1,0),
       (0,1,0,1,1,0,1,1,0),
   )
    assert validar_5_filas_ocupadas(mi_carton) == True

def test_dosvacias_consecutivas():
    mi_carton = (
       (1,0,1,0,1,0,1,1,0),
       (1,0,1,0,1,0,1,1,0),
       (0,1,0,1,0,0,1,1,0),
   )
    assert validar_dosvacias_consecutivas(mi_carton) == True

def test_dosocupadas_consecutivas():
    mi_carton = (
       (1,0,1,0,1,0,1,1,0),
       (1,0,1,0,1,0,1,1,0),
       (0,1,0,1,0,0,1,1,0),
   )
    assert validar_dosocupadas_consecutivas(mi_carton) == True
