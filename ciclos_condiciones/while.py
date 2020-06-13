numero = int(input("Ingrese el numero?"))
contador = 0

while numero >= 1:
    contador+=1
    numero = numero /10
else:
    print("La cantidad de digito es ", contador)
