#!/usr/bin/env python 3.7

alfabeto = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
    'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
    'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w':23, 'x': 24, 'y': 25, 'z': 26
}
frase = input("Ingresa tu frase: ")
# Variables que utilizaremos para almacenar
# el cofigo de la frase y el formato de salida.
codigo = ''
formato = ''

# Buscando las letras en el alfabeto
# para localizar su codigo
for letra in frase:
    if letra in alfabeto.keys():
        codigo += str(alfabeto[letra])
        formato += f"{letra}({str(alfabeto[letra])}) "

print(codigo, formato)