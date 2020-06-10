"""
Lista de objetos, = se permite guardar opjetos de tipos diferentes pero la recomendacion es que sean del mismo tipo
para crear una lista es solo darle un nombre a la variable seguido por la el signo igual y los brackets []
Para acceder a los datos se debe hacer por los indices donde 0 es el primero y el ultimo la longitud de la lista 1
"""
cursos = ["C#","Python","JavaScripts","Java","GO","PHP", "TypeScripts","c"]

# Para Acceder indice 0
print("Primero",cursos[0])

# Longitud
print("Longitud", len(cursos))

"""
tambien pytho acepta indice invertidos por ejemplo el -1
"""
print("Leer de forma invertida", cursos[-2])


#Ultimo registro
print("Utilmo", cursos[len(cursos)-1])

#Traer toda la lista
print("Toda la lista", cursos[:])

#Traer los primer hasta un indice x
print("Cursos desdel primero hasta el 3", cursos[0:3])

#Traer apartir del indice 0
print("A partir del indice  0",cursos[0:])

#traer desde el indice 3 hasta el 5
print("A partir del indice 2 hasta el 5",cursos[2:5])

#Traer los datos desde el 1 hasta el 5 con saltos de 2
print("Solo 1,3,5", cursos[1:5:2])

#Invertir la listas
print("Inversio", cursos[::-1])

