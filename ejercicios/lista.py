lista = []
contador = 0

while True:
    numero = int(input("Ingresar valor\n"))
    lista.append(numero)
    contador+= 1
    if contador >= 9:
        break


suma = 0
contador= 0
while contador<len(lista):
    suma += lista[contador]
    contador += 1


print("suma",suma)
print("Promedio",suma/len(lista))
print("Numero menor", min(lista))
print("Numero Mayor",max(lista))