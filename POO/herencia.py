class Animal:
    def __index__(self, nombre):
        self.nombre = nombre
    def comer(self):
        print("Comiendo")
    def domir(self):
        print("Durmiendo")

class Perro(Animal):
    def __int__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("Ladrando")


fperro = Perro()
fperro.comer()
fperro.domir()
fperro.ladrar()