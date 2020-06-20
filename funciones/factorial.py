def factorial(numero):
    if numero > 1:
        numero = numero * factorial(numero-1)
    print("Valor numerico", numero)
    return numero

if __name__ == "__main__":
    print(factorial(2))