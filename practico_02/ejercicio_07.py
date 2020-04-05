# Programe una clase EJERCICIO tiene los siguientes métodos
#  INICIO se le pasa una fecha y devuelve el 1 de Julio anterior.
#  FIN se le pasa una fecha y devuelve el 30 de Junio próximo.
#  SEMANA devuelve el nro de semana contando a partir del 1 de Julio anterior.
import datetime
from math import ceil

class Ejercicio(object):

    def InicioDate(self, date):
        date1 = datetime.datetime(date.year-1,7,1)
        date2 = datetime.datetime(date.year,7,1)
        return date1 if date < date2 else date2

    def Inicio(self, date_string):
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
        return self.InicioDate(date).strftime("%d/%m/%Y")

    def FinDate(self, date):
        date1 = datetime.datetime(date.year,6,30)
        date2 = datetime.datetime(date.year+1,6,30)
        return date1 if date < date1 else date2

    def Fin(self, date_string):
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
        return self.FinDate(date).strftime("%d/%m/%Y")

    def Semana(self, date_string):
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
        date1 = self.InicioDate(date)
        return ceil(((date-date1).days+1)/7)

ej = Ejercicio()
assert ej.Inicio("01/02/2017") == "01/07/2016"
assert ej.Inicio("22/11/2017") == "01/07/2017"
assert ej.Fin("01/02/2017") == "30/06/2017"
assert ej.Fin("22/11/2017") == "30/06/2018"
assert ej.Semana("01/02/2017") == 31
assert ej.Semana("02/11/2017") == 18
