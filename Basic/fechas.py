#Fechas es necesario importar las dependencias necesarias
from datetime import date
from datetime import datetime

#Dia actua
today = date.today()
now = datetime.now()

print("Hoy es {0}".format(date.today()))
print("Fecha actual {0}".format(datetime.now()))

#Date
print("Dia {0}".format(today.day))
print("Mes {0}".format(today.month))
print("Año {0}".format(today.year))

#Datetime
print("El día actual es {}".format(now.day))
print("El mes actual es {}".format(now.month))
print("El año actual es {}".format(now.year))

print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))