# Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
# - print_data(): imprime por pantalla toda la información del objeto.
# - generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni.
from random import randint

class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.generar_dni()

    def es_mayor_edad(self):
        return self.edad >= 18

    def generar_dni(self):
        self.dni = randint(10000000, 99999999)

    def print_data(self):
        print("{0.nombre}\nDNI: {0.dni}\nEdad: {0.edad}\nSexo: {0.sexo}\nPeso: {0.peso}\nAltura: {0.altura}"
        .format(self))

if __name__ == "__main__":
    p = Persona("Juan", 20, "M", 56, 1.90)
    assert p.es_mayor_edad()
    p.print_data()