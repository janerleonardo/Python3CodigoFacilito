def saludo(nombre : str) ->None:
    print("Hola mundo " + nombre)
def suma(val : int ,val1: int = 0) -> int:
    return val+ val1

print(suma(10,20))
print(saludo("Janer"))