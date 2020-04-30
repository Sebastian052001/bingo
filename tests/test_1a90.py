from src.bingo import carton

def test_uno_a_noventa():
    mi_carton = carton()
    for fila in range(0,2):
        for columna in range(0,8):
          celda = mi_carton[fila][columna]
          assert celda >= 0 and celda <=90
