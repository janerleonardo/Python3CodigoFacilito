"""
Se puede asignar una funcion a variable  de la siguiente manera se crea la variable y se igual a la funcion sin los
paretesis
"""
def centigrados_farhenheit(grados):
    return grados * 1.8 +32

function_variable= centigrados_farhenheit
resultado = function_variable(32)
print(resultado)