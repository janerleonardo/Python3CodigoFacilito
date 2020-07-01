"""
Getter y Setter utilizando la funcion property, no recibe nada en el contructor y se define las respectivas funciones
set_age y get_age y se  envian como parametros a a funcion property(), de esta forma  se esconde mucho mas la variable
privada
"""

class Geeks:
    def __init__(self, age=10):
        self._age = age

    # function to get value of _age
    def get_age(self):
        print("getter method called")
        return self._age

    # function to set value of _age
    def set_age(self, a):
        print("setter method called")
        self._age = a

    # function to delete _age attribute
    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age)


mark = Geeks(50)

mark.age = 10

print(mark.age)

mark._age= 20
print(mark._age)

