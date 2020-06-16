"""
Cuando se necesita modificar una funcion existente sin cambiar sus lineas de codigo, para ello se utiliza los decoradores
las funcione son a,b,c donde a(b) -> c
"""
def decorador(funcion):
    def nueva_funcion(*args, **kwargs):
        print("Podemos agregar codigo antes")
        resultado = funcion(*args, **kwargs)
        print("Podemos agregar codigo despues")
        return resultado
    return nueva_funcion

@decorador
def funcion_a_decorar():
    print("Esta es una funcion a decorar")

@decorador
def suma(val, val1):
    return val + val1

funcion_a_decorar()

print("\n")

resultado = suma(20,10)
print(resultado)