"""
Si se quiere cambiar la variale que ingresa por parametro a una funcion debemos utilizar la pañlabra reservada
nonlocal
"""
def comenzar_play_list(lista):
    def reproducir():
        for val in lista:
            print(val)
    reproducir()

lista = ["Rapido y Furioso","Rambo","Taken 1", "Amores de verano"]
print(comenzar_play_list(lista))

def comenzar_play_list1(lista1):
    print(lista1)
    lista1 = [1,2,3]
    def reproducir1():
        for val in lista:
            print(val)
    reproducir1()

lista1 = ["Rakie 3 ","no es una estupida pelicula americana","American Pie"]
print(lista1)
print("Sin nonlocal", comenzar_play_list1(lista1))

"""""
def comenzar_play_list_nonlocal(lista):
    nonlocal lista
    lista = [1,2,3]
    def reproducir():
        for val in lista:
            print(val)
    reproducir()

print("Con nonlocal", comenzar_play_list_nonlocal(lista))
"""""
