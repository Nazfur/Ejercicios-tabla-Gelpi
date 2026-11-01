def func_matriz(operacion="crear", *args):

    valores = []
    if len(args) == 3: valores = args[2]

    def constructor_matriz(tamaño_de_matriz, valores=None, no_tocar=0):
        try:
            valores[0] = valores[0]
            valores = valores[:]
        except:
            raise ValueError("Error en el constructor de matriz, valores no es una lista")

        matriz = {
        "tamaño": tamaño_de_matriz,
        "datos": [0] * tamaño_de_matriz[0] * tamaño_de_matriz[1] if valores is None else valores
        }
        return matriz
    def mod_matriz(matriz, pos, valor):
        matriz["datos"][pos[1] * matriz["tamaño"][0] + pos[0]] = valor
        return matriz
    def ver_valor_matriz(matriz, pos, no_tocar=0):
        return matriz["datos"][pos[1] * matriz["tamaño"][0] + pos[0]]

    operaciones = {"crear":constructor_matriz, "mod":mod_matriz, "ver":ver_valor_matriz}

    return operaciones[operacion](args[0], args[1], valores)


'''
Documentacion para func_matriz:

Solo para matrices cuadrada!!

Es una funcion que tiene dos operaciones crear una matriz desde cero con sus valores
o todo 0, y modificar cada uno de sus valores, la funcion mejora el rendimiento y la
compresion del programa haciendolo más mantenible.

func_matriz(operacion, argumentos), esta es su sintaxis basica, a final devuelve
la siguiente estructura:
{tamaño:(x, y), valores:[a, b, c, d, e, f, ...]}

mi_matriz = func_matriz("crear", tamaño:(x, y), valores:[a, b, ...])

Crea la estructura de datos matriz y la guarda en la variable, no es necesario poner
valores, en caso de que no se especifiquen lo rellanara con ceros.

mi_matriz = func_matriz("mod", mi_matriz, posicion:(x, y), valor)

Esto modifica el valor de la posicion x e y por el valor pasado.

func_matriz("ver", mi_matriz, posicion:(x, y)) devuelve el valor de la posicion x e y
de mi_matriz.


'''

