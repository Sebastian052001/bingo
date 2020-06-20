from src.bingo import intentoCarton

def test_longitud_carton():
    mi_carton = intentoCarton()
    bool_Longitud = True
    if len(mi_carton) != 9:
        bool_Longitud = False
    else:
        for x in range(0,9):
            if(len(mi_carton[x]) != 3):
                bool_Longitud = False
    assert bool_Longitud == True