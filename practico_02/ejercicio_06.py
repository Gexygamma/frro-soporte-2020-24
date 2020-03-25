# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).
from datetime import datetime

class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.nacimiento = nacimiento

    def edad(self):
        hoy = datetime.now()
        return hoy.year - self.nacimiento.year - ((hoy.month, hoy.day) < (self.nacimiento.month, self.nacimiento.day))

assert Persona(datetime(1998, 2, 2)).edad() == 22