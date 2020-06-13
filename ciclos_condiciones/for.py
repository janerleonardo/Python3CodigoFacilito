numeros = [1,2,3,4,5,6,7,8,9]

for numero in numeros:
    print(numero)

diccionario = {'a':1, 'b':2}

for llave in diccionario:
    print(llave)

for llave,valor in diccionario.items():
    print("llave {0}, {1}".format(llave,valor))

valores = ((10,20,30),["a","b",'c'],(None,True,False))

for valor in valores:
    for v in valor:
        print(v)

for valor1, valor2, valor3 in valores:
    print(valor1,valor2,valor3)