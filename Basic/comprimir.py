"""
Se tyrabajar con la funcion zip -> función devuelve un iterador de tuplas basado en los objetos iterables.
                            tuple-> incorporado se puede utilizar para crear tuplas en Python.
                            list ->
"""

#tupla con zip
tupla = tuple(zip())
print("Tupla con zip",tupla)

tupla1 = (1, 2, 3, 4)
lista =[10, 20, 30, 40, 50]
resultado = zip(tupla1,lista)
print(resultado)
#convertimos el objeto zip en tupla
resultado1 = tuple(resultado)
print(resultado1)
#Convertimos el objeto en lista
resultado = zip(tupla1,lista)
resultado2 = list(resultado)
print(resultado2)

