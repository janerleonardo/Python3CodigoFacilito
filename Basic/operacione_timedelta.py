"""
timedelta es un objeto que sirve para representar tiempo y realizar operaciones con ese tiempo
su parametros son days, seconds, microseconds, milliseconds, minutes, hours, weeks
"""

from datetime import datetime
from datetime import timedelta



#Sumar dias
now = datetime.now()
new_date = now + timedelta(days=2)

print("suma 2 dias {0}".format(new_date))

# Sumar mese
new_date =  now +timedelta(weeks=1)
print("Sumar 1 semana {}".format(new_date))

