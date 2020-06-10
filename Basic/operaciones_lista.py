"""
Utilizacion del metodo de ordenamiento sort() y los metodos min y max
"""
lista = [8,17,90,1,5,44,1.32]

#Impresiones.
print(lista[:])

#Ordenar con sort
lista.sort()
print("Ordenado\n", lista)

#Ordenamiento  descendente
lista.sort(reverse=True)
print("Ordenamiento desc\n", lista)


#Max
print("numero Maximo\n", max(lista))

#Min
print("Minimo\n",min(lista))

#Buscar en la lista
print("Esta el numero 8?\n", 8 in lista)

#cual es el indice en la lista
print("Indice", lista.index(44))

#Metodo count
print("Cuanos 5 hay en la lista\n", lista.count(5))




