def factorial(numero):
    if numero > 1:
        numero = numero * factorial(numero-1)
    print("Valor numerico", numero)
    return numero


print(factorial(2))