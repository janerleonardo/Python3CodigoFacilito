"""
En esta opcion Utilizaremos los getter y los setter con @property  y @age.setter, te esconde la variable sin embargo la
varable sigue siendo accesible si se conoce el nombre
"""
# @property

class Geeks:
    def __init__(self):
        self._age = 0

    # using property decorator
    # a getter function
    @property
    def age(self):
        print("getter method called")
        return self._age

        # a setter function

    @age.setter
    def age(self, a):
        if (a < 18):
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._age = a


mark = Geeks()

mark.age = 19

print(mark.age)

mark._age = 30
print(mark._age)
