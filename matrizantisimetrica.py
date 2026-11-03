def es_antisimetrica(matriz:list) -> bool:

    for ind_x, lista in enumerate(matriz):
        for indx_y, valor in enumerate(lista):
            if ind_x == indx_y and valor:
                return False
            else:
                if matriz[indx_y][ind_x] + valor == 0:
                    return False
    return True