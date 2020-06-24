def fibonacci(number):
    if number == 0: return 0
    elif number == 1:return 1
    else: return fibonacci(number -1) + fibonacci(number - 2)

def palindromo(sentence):
    """Funcion Palindromo para validacion
    :param sentence: String o Entero
    :return: True o False
    >>> palindromo("anita lava la tina")
    True
    """
    sentence = str(sentence).lower().replace(" ", "")
    return sentence == sentence[::-1]

def factorial (number):
    if number == 0: return 1
    else: return number * factorial(number -1)
    