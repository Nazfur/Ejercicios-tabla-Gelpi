def cambio_monetario(centimos):
    cantidad = centimos

    monedasTipos = [20, 10, 5, 2, 1]
    cantidadMonedas = [0] * len(monedasTipos)


    for moneda, indice in enumerate(monedasTipos):
        
        cantidadMonedas[indice] = cantidad // moneda
        cantidad = cantidad - cantidadMonedas[indice] * moneda
    
    return tuple(cantidadMonedas)
