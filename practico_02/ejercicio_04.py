# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).
from practica_02.ejercicio_03 import Persona
from datetime import datetime

class Estudiante(Persona):

    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        super().__init__(nombre, edad, sexo, peso, altura)
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas

    def avance(self):
        return self.cantidad_aprobadas / self.cantidad_materias

    # implementar usando modulo datetime
    def edad_ingreso(self):
        return self.edad - (datetime.now().year - self.anio)

if __name__ == "__main__":
    e = Estudiante("Juan", 20, "M", 56, 1.90, "ISI", 2018, 50, 20)
    assert e.edad_ingreso() == 18
    assert e.avance() == 0.40