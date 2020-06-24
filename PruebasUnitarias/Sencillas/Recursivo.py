"""
>>> recursivo = Recursivo()
>>> recursivo.factorial(5)
120
"""
class Recursivo:
    def factorial (self, number):
        if number == 0: return 1
        else: return number * self.factorial(number -1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

