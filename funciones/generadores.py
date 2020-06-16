"""
Los generadores es un tipo  especial de funcion para generar una serie de datos los cuale podemos iterar
o utilizar como desemos
range-> genera numero desde el primer parametro hast el segundo
yield -> returno el resultado sin termina la funcion de la esta ejecutando diferente al return
"""
def tabla_multiplicar(numero,maximo=10):
    """Gnerador de tablas de muliplicar, Ideal para aprender a hacer de memoria"""
    for posicion in range(1,maximo+1):
        yield numero * posicion
for resultado in tabla_multiplicar(9):
    print(resultado)

print(tabla_multiplicar.__doc__)