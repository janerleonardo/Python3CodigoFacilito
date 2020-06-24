def palindromo(sentence):
    """Funcion Palindromo para validacion
    :param sentence: String o Entero
    :return: True o False
    >>> palindromo("anita lava la tina")
    True
    """
    sentence = str(sentence).lower().replace(" ", "")
    return sentence == sentence[::-1]


if __name__ == "__main__":
    palindromo(121)