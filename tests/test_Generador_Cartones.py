from src.bingo import carton
from src.bingo import intentoCarton
from src.bingo import transformar_carton
from src.bingo import pruebas_carton
from src.bingo import carton_definitivo

def test_longitud_carton():
    bool_Longitud = True
    mi_carton = carton()
    if len(mi_carton) != 3:
        bool_Longitud = False
    else:
        for x in range (0,3):
            if len(mi_carton[x]) != 9:
                bool_Longitud = False
    assert bool_Longitud == True

def test_longitud_carton_intentoCarton():
    mi_carton = intentoCarton()
    bool_Longitud = True
    if len(mi_carton) != 9:
        bool_Longitud = False
    else:
        for x in range(0,9):
            if(len(mi_carton[x]) != 3):
                bool_Longitud = False
    assert bool_Longitud == True

def test_transformar_carton():
    bool_Longitud = True
    mi_carton = intentoCarton()
    if (len(transformar_carton(mi_carton))) != 3:
        bool_Longitud = False
    else:
        for x in range(0,3):
            if(len(transformar_carton(mi_carton)[x]) != 9):
                bool_Longitud = False
    assert bool_Longitud == True

def test_evaluaciones_carton():
    carton_transformado = (
        [0,18,0,32,42,0,60,71,0],
        [0,19,23,0,46,0,63,79,0],
        [1,0,29,35,0,54,0,0,84]
    )    
    assert pruebas_carton(carton_transformado) == True

def test_carton_defintivo():
    bool_Longitud = True
    mi_carton = carton_definitivo()
    if (len(mi_carton) != 3):
        bool_Longitud = False
    else:
        for x in range(0,3):
            if(len(mi_carton[x]) != 9):
                bool_Longitud = False
    assert bool_Longitud == True