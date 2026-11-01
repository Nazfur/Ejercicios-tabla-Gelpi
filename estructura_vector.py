def vector(*args, ser_dato_vector=False, valor_vector=(0,0)):

    if len(args) == 1: ser_dato_vector = -1 # Para saber si se está pasando un argumento de orden

    # Funcion constructor, construye el dato vector
    def constructor_dato(x, y):
        try: # Mejor que comprobar repetidamente con type(), acepto valores int, float, bool
            x = x + 0
            y = y + 0

        # Si salta es costoso, pero no deberia de hacerlo nunca, es un error critico que rompe el programa antes
        # para que se corrija el error.
        except:
            raise ValueError("Los datos introducidos no son correctos, asegurese de usar int, float o bool")

        return vector(x, y, ser_dato_vector=True)
    #-------------------------------------------------------------------------------------

    # Funciones para operar con datos vectores
    def mostrar(v1):
        return v1["valor_vector"]
    def sumar(v1, v2):
        v1 = mostrar(v1)
        v2 = mostrar(v2)
        return {"valor_vector":(v1[0] + v2[0], v1[1] + v2[1]), "ser_dato_vector":2}
    def restar(v1, v2):
        v1 = mostrar(v1)
        v2 = mostrar(v2)
        return {"valor_vector":(v1[0] - v2[0], v1[1] - v2[1]), "ser_dato_vector":2}
    def multiplicar(v1, multiplo):
        v1 = mostrar(v1)
        return {"valor_vector":(v1[0] * multiplo, v1[1] * multiplo), "ser_dato_vector":2}
    #--------------------------------------------------------------------------------------

    # Definir las operaciones en un diccionario

    '''
    Esto luego permite retornar la funcion segun el parametro elegido
    ejemplo:

    return tipo_de_operaciones[operador]

    Entonces vector("sumar")() pasa a ser sumar()
    '''

    tipo_de_operaciones = {
        "sumar":sumar,
        "restar":restar,
        "multiplicar":multiplicar,
        "mostrar":mostrar
        }
    #-----------------------------------------

    # Evalua el tipo de dato que es vector

    '''
    Según el tipo de dato de vector, devuelve su forma final o lo pasa por el constructor

    En el caso -1: No es un tipo de dato vector si no una orden
    y devuelve la funcion que corresponde.

    En el caso 0 se trata de una entrada directa de los valores;
    x e y, y se pasa por el constructor para generar el diccionario completo
    '''

    match ser_dato_vector:
        case -1:
            return tipo_de_operaciones[args[0]]
        case 0:
            return constructor_dato(args[0], args[1])
        case 1:
            return {"valor_vector":(args[0], args[1]), "ser_dato_vector":2}
        case _:
            raise ValueError("Error en el tipo de dato vector, no se identifica")

'''
Documentación:

    La función vector hay que entenderla como una estructura de datos;

    vector(0, 1) -> Genera una estructura vector, en el fondo es una libreria
    valor_vector = (x, y) y si es un dato vector. Este ultimo atributo sirve
    para controlar las entradas, quiero que mi funcion vector trabaje con vectores.
    y no quiero meterle una tupla directa, para que quede claro que se está metiendo

    a = vector(1, 0) -> Esto es "igual" que hacer a = int(1)
    le asignas a a el valor vector(1,0)

    vector(operacion)(argumentos) -> Esto es la sintaxis para operar con vectores;
    es decir:
    a = vector("sumar")(a, vector(1, 2)) -> Lo que va a hacer es sumar el vector a con el vector(1, 2)
    y su salida va a ser tipo vector, es decir vector(2, 2).
    Y si se quiere utilizar como una tupla para pasarlo como indice de una matriz:
    vector("mostrar")(a) -> (2, 2) te devuelve una tupla.
'''


