"""
La funcion map, permite aplicar una funcion sobe los items de un objeto iterable(Lista, tuplas, Diccionario)
"""
def cuadrado(numero):
    return numero * numero

lista = [1,2,3,4,5,6]
resultado = list(map(cuadrado, lista))

print(resultado)


resultado1 =  list(map(lambda numero : numero * numero,lista))
print(resultado1)