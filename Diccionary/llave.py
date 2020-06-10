"""
los diccionarios como las cadenas permite tanto comillas doble como simples
"""
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,'f': 6, 'g': 7, 'h': 8 }

#obtner todas las llaves
print(diccionario.keys())

#Obtener los valores
print(diccionario.values())

#Obtener las llaves como los valores retorna cada llave valor como tuplas
print(diccionario.items())

#Eliminar llaves ambos eliminan
del diccionario["a"] # funcion del
diccionario.pop("b") # Metodo pop
print(diccionario)

#Limpiar diccionario
diccionario = {}
diccionario.clear()
print(diccionario)
