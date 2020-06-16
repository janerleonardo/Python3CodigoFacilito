"""
Asignadole el decorador @staticmethod vuelves al metodo estatico por lo tanto no es necesario la palabr self
el uso de los metodos estaticos nos pérmiten crear clases mas independiente y que sea reutilizables
"""
class Triangulo:
    numero = 2
    def __init__(self, base=0,altura=0):
        self.base = base
        self.altura = altura
    def __str__(self):
        return "Clase para Calcular el area de n circulo"
    def area(self):
        return self.base * self.altura / Triangulo.numero
    @staticmethod
    def area_statica(base, altura):
        return base*altura/Triangulo.numero

triangulo = Triangulo(20,30)
print(triangulo.area())
print(Triangulo.area_statica(20,30))
print(triangulo)
print(triangulo.__dict__)
print(Triangulo.__dict__)