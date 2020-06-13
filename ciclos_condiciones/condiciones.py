"""
Condicion if utilizando las comillas simples y comillas dobles
los datos que pytho toma como false son False, "", '',  [], (), {}, 0, 0.0, None
"""
color_luz = "rojo"
if color_luz == 'verde':
    print("Puede continuar")
elif color_luz == 'rojo':
    print("Color rojo")
else:
    print("No puede continuar")

variable = None
if variable :
    print("Verdadero")
else:
    print("False")

