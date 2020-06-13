#!/usr/bin/env python3.7

# JulianV
# Jan 25 2020.
# Listar los numeros pares del 1 al 100
print()
print("numeros pares del 1 al 100".title().center(40,'-'))
# buscando los numeros pares
# dentro del rango de 1 a 100.
for numero in range(1, 101):
    # si el reciduo es = 0
    # muestralo en pantalla.
    if numero % 2 == 0:
        # Formateando los datos de salida.
        print(f"\t\t{numero}")
