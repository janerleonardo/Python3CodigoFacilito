"""
Las Tuplas son una estructura de datos parecido a  a las lista con la diferencia de que estatico es decir 
no se puede modificar,  al ser estatico la hace mucho mas rapido

"""""
tupla = (1,2,3,4,5,6,7,8,9)

#obtener valor
print("Obtengo valor ", tupla[0])

#obtener valor por indice negativo
print("Obtener valor con -1", tupla[-1])

#obtener sub tupla con salto de 2
print("Sub tupla", tupla[0:5:2])

#Comprimir Tupla y asignara a variable con la multi-asignacion
uno,dos,tres,cuatro = tupla[0], tupla[1], tupla[3], tupla[4]


print(tres)
print("Valores", uno )
print("Dos",dos)
print(cuatro)


#Otra forma el numero de variable debe ser igual al numero de datos de la tupla
tupla1 = (1,2,3)
cinco, seis, siete = tupla1
print(cinco)
print(seis)
print(siete)

#Funciona con lista si funciona igual
lista = [1,2,3]
a, b, c, = lista
print("datos {0} {1} {2}".format(a,b,c))


