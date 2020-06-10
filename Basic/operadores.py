variable_uno = 10
variable_dos = 18

mayor = variable_uno > variable_dos
menor = variable_uno < variable_dos
mayor_igual = variable_uno >= variable_dos
menor_igual = variable_uno <= variable_dos
igual = variable_uno == variable_dos
diferente = variable_uno != variable_dos

print(mayor)
print(menor)
print(mayor_igual)
print(menor_igual)
print(igual)
print(diferente)

resultado = True and True and diferente
print("and {0}".format(resultado))

result = True or True or diferente
print("or {0}".format(result))

resul = not False
print("not False {0}".format(resul))

num = variable_uno is variable_dos
print("Is {0}".format(num))




