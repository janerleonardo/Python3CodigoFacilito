#!/usr/bin/env python 3.7
"""
Forma de poner un numero indefinido de parametros, se realizaria con el * y por convencion seguido de la palabra args
que es una tupla
"""

def suma(Cadena,*args):
    total= 0
    print(Cadena)
    for numero in args:
        total += numero
    return total

print(suma("Suma",10,20,30,40,50,60))

"""
Tambien se le puede asignar parametros indefinido con doble ** y por convesionla palabra kwargs
te crear un diccionario, por lo tanto debes agregar cada parametros con la la llave ejemplo cod="Janer"
"""
def usuario_autenticado(**kwargs):
    print(kwargs)

usuario_autenticado(cod="Janer",valor= True,entero=123,dicimall=2.3)

"""
Combianacion de funcionaes estandar, con *args y *kwargs 
"""
def combinacion(requerido, conDefault='',*args,**kwargs):
    print(requerido)
    print(conDefault)
    print(args)
    print(*args)
    print(kwargs)


combinacion("Valor Requerido",10,10,20,30,45,valor="Janer",Valor2="Leonardo")