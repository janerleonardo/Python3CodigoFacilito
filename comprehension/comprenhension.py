lista =[]
for x in range(0,101):
    lista.append(x)

print(lista)

estructura = [ x for x in range(0,101) if x % 2 == 0]
print(estructura)

tuplas = tuple(( x for x in range(1,101) if x % 2 == 0))
print(tuple)

diccionario = { indice:valor  for  indice, valor in  enumerate(estructura)}
print(diccionario)