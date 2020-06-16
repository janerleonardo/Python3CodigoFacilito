"""
Los metodos de clase son aquellos que se decoran con @classmethod, por convencion se utiliza la pabla cls que vendia a
ser como el self en los metodos de instacion, comumente se utilizza cuando queremos utilizar variables de Clase
"""
class Circulo:
    PI=3.14159265
    @classmethod
    def area(cls,radio):
        return cls.PI * radio**2

print(Circulo.area(10))
