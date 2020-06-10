#Comentarios de codigo
nombre = input("¿Cual es tu nombre?\n")
"""
Comentarios de Parrafos un pco loco no crees?
"""
edad = int(input("¿Cúal es tu edad?\n"))

peso = float(input("¿Cual es tu peso?\n"))

autorizado = input("¿Estas autorizado?\n") == "si".upper()

print("Hola {0}, Edad {1}, Peso {2}, Autorizado {3}".format(nombre,edad,peso,autorizado))
