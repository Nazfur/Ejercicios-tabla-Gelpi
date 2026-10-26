def cambio_monetario(centimos):
    cantidad = centimos

    monedasTipos = [20, 10, 5, 2, 1]
    cantidadMonedas = [0] * len(monedasTipos)

    indice = 0

    for moneda in monedasTipos:
        
        cantidadMonedas[indice] = cantidad // moneda
        cantidad = cantidad - cantidadMonedas[indice] * moneda
        indice += 1
    
    return cantidadMonedas
