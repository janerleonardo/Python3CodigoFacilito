"""
Existen 2 tipos de variable, las variables de clase,y variable de instancia las variable de instancia, son las que se
define con la palabra feld de acuerdo a convenciones, las varaible de clase no necesitan tner una instacion para ser usado
"""
class Circulo:
    PI = 3.14159265
    def __init__(self, radio):
        self.radio = radio # Variable de Instacia

circulo_a = Circulo(30)
circulo_b = Circulo(10)

print(circulo_a.radio)
print(circulo_b.radio)
print(circulo_a.PI)
print(circulo_b.PI)

circulo_b.radio = circulo_a.radio*20
circulo_a.PI = circulo_b.PI*2
print(circulo_b.radio)
print(circulo_a.PI)
#Sin Instacion un Objeto de la clase
print(Circulo.PI)
