"""
Pueden existir dos variables diferentes con el mismo nombre en un scripts de python, si una es global y la otro local
con la palabra reservada global, puedes decirle a python que la variable que vas a modificar es la varible global
"""
animal = 'Leon' #Variable  global

def animales():
    animal='Ballena' # variable local
    print(animal)
animales()
print(animal)
def zoo():
    global animal
    animal = 'Tigre'
    print(animal)
zoo()
print(animal)