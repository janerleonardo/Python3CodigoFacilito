texto = "curso de Python 3"
texto1 = " curso de Python 3 y  Python 2 "
print("Mayuculas",texto.upper())
print("Minuscula",texto.lower())
print("Campitalize", texto.capitalize())
print("Swapcase", texto.swapcase())
print("Es minuscula? ",texto.islower())
print("Es mayuscula? ",texto.isupper())
print("title crea un string con formato de titulo ",texto.title())
print("Replace con cantidad de replace", texto1.replace("Python","Java",1))
print("strip quita los espacio a derecha e izquierda", texto1.strip())
curso = "Python"
version = 3
version_1 = 1

print("Curso de %s %s %s"%(curso,version,str(version_1)))