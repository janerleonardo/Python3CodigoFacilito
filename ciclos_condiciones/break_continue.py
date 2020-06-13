"""
El Break para abruntamente el ciclo,
el continue salta a la siguiente iteracion
"""
titulo = "Curso de Python 3"
for caracter in titulo:
    if caracter == "P":
        break
    print(caracter)
print("Siguiente")
for caracter in titulo:
    if caracter == "P":
        continue
    print(caracter)