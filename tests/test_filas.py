from src.bingo import carton

def test_fila():
    mi_carton=carton()
    for x in range(0,2):
        filas_ocupadas = 0
        for y in range(0,8):
            filas_ocupadas += mi_carton[x][y]
        assert filas_ocupadas > 0

