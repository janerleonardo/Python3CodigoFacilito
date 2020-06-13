#!/usr/bin/env python3.7


palindromos = []

print("Teclea 4 frase, tedire si es un palindromo.")
count = 1
while count <= 4:
    frase = input("Frase--> ")
    if frase == frase[::-1]: #palind_frase:
        palindromos.append(frase)
    else:
        print("Lo siento, no es palindromo")
    count += 1

print("")
print("Los palindromos son los siguientes.".center(20,'-'))
for palindromo in palindromos:
    print(f"\t{palindromo}")
