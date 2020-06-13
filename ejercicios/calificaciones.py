calificaciones = {"calculo":10, "dibujo":5,"Sistemas":9, "Matematicas": 3, "Castellano": 2}
promedio = 0
for  key, calificacion in calificaciones.items():
    promedio += calificacion
    if calificacion > 5:
        print(key,calificacion)
print(promedio/len(calificaciones))

