"""
La funciones lambda son funciones expresadas en una solo licea de codigo, para crear una funcion de este tipo
se debe utilizar la palabra reservada lambda  seguido de los parametros qe puede tener default, : (Dos puntos)
lo que quereos quee haga la funcion, todas la fucionees lambdas retornan un valor
"""
my_funcion = lambda grados=0: grados * 1.8 +32

print(my_funcion())

sin_parametros = lambda : True

print("True",sin_parametros())

con_valores = lambda val, val1=10, val2=10 : val + val1 + val2

print("Suma",con_valores(20))

con_asterisco = lambda *args : args[:]

print("Tupla",con_asterisco(10,20,30,40))

con_doble_asterisco = lambda **kwargs : kwargs["janer"]

print("Asteri",con_doble_asterisco(janer=0))

con_asteriscos = lambda *args , **kwargs : kwargs.get('key', False)
print(con_asteriscos(10,10,10,10,key=32))