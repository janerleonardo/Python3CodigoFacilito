"""
Una funcion por defecto termina cuando la ultima linea se haya ejecutado,
Si la funcion no tiene la palabra reservada return  la funcion devuelve None
Si tiene la plabara reservada return termina cuando se ejecute esa linea
"""

def function_without_rertun():
    print("Mensaje")

print(function_without_rertun())

def function_with_return():
    return 2
print(function_with_return())

#Valores Falso "",'',0,{},(),[],None,False
def function_janer(parametro):
    if parametro:
        return 100

print(function_janer(0))