"""
Las funciones recursivas son las funciones que se llaman a ellas mismas, se deben controlar para que no se queden
ciclos infinitos
"""
def funcion_recursiva(numero):
    numero -=1
    if numero > 0:
        print("Numero Positivo",numero)
        funcion_recursiva(numero)
    else:
        print("Numero Negativo")
    print("Salimos")

funcion_recursiva(5)
