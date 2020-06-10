"""
Calendar iFunciones Generales relacionada con el calendarios
funciones interesantes
    setfirstweekday = Estable el dia de la semana por defecto esta lunes (0)
    firtweekDay() = Devuelve la configuracion actual del primer dia de la semana
    isleap(año) = devuelve si el año es bisiesto (true o false segun el caso)
    weekday(año,mes,dia0) = devuelve el dia de la semana
"""
import calendar

#firstweekday
print("Primer dia de la semana {}".format(calendar.firstweekday()))

calendar.setfirstweekday(calendar.SUNDAY)
print("Primer dia de la semana domingo {}".format(calendar.firstweekday()))

#Ano Bisieto 2020
print("Año bisiesto {}".format(calendar.isleap(2020)))



