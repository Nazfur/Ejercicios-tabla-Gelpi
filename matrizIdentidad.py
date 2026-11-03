def esCuadrada(matrix):
    return True if len(matrix) == len(matrix[0]) else False

def esMatrizIdentidad(matrix):
    
    if not esCuadrada(matrix):
        return False
    
    for indice, lista in enumerate(matrix):
        
        if not sum(lista) == 1:
            return False
        if not lista[indice] == 1:
            return False
        if not 0 in lista:
            return False
    
    return True





if __name__ == "__main__":


    matrix1 = [
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]]

    assert esMatrizIdentidad(matrix1)
    #>>>True

    matrix2 = [[1,0,0],
            [0,1,0],
            [0,0,0]]

    assert not esMatrizIdentidad(matrix2)
    #>>>False

    matrix3 = [[2,0,0],
            [0,2,0],
            [0,0,2]]

    assert not esMatrizIdentidad(matrix3)
    #>>>False

    matrix6 = [[1,0,0,0],  
            [0,1,0,2],  
            [0,0,1,0],  
            [0,0,0,1]]

    assert not esMatrizIdentidad(matrix6)
    #>>>False

    matrix7 = [
            [1, -1, 1],
            [0, 1, 0],
            [0, 0, 1]]
    assert not esMatrizIdentidad(matrix7)
    #>>>False           


    # casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert):

    matrix4 = [[1,0,0,0],
            [0,1,1,0],
            [0,0,0,1]]

    assert not esMatrizIdentidad(matrix4)
    #>>>False

    matrix5 = [[1,0,0,0,0,0,0,0,0]]

    assert not esMatrizIdentidad(matrix5)
    #>>>False       
      