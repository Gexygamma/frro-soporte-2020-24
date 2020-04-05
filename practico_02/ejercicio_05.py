# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from practica_02.ejercicio_04 import Estudiante


def organizar_estudiantes(estudiantes):
    dct = dict()
    for e in estudiantes:
        if not e.carrera in dct.keys():
            dct[e.carrera] = 1
        else:
            dct[e.carrera] += 1
    return dct

lista_estudiantes = [
    Estudiante("Juan", 20, "M", 56, 1.90, "ISI", 2018, 50, 20),
    Estudiante("Pedro", 21, "M", 51, 1.70, "IQ", 2019, 50, 10),
    Estudiante("Ana", 19, "F", 55, 1.85, "IQ", 2017, 50, 30),
    Estudiante("Carla", 22, "F", 60, 1.75, "IM", 2017, 50, 30)
]

assert organizar_estudiantes(lista_estudiantes) == {'ISI': 1, 'IQ': 2, 'IM': 1}