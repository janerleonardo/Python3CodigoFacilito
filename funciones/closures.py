"""
Closures es una funcion genere dinamicamente una funcion y que esta funcion pueda acceder a las variables locales
en el cajo de ejemplo en la linea 12 estamos ejecutando la funcion  mostrar_mensaje pero

"""
def mostrar_mensaje(mensaje):
    mensaje = mensaje.upper() # local
    def mostrar():
        print(mensaje)
    return mostrar

nueva_funcion = mostrar_mensaje("janer")
nueva_funcion()