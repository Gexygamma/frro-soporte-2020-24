# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime

from ejercicio_01 import crear_conexion, reset_tabla

def agregar_persona(nombre, nacimiento, dni, altura):
    conn, curs = crear_conexion()
    values = (nombre, nacimiento, dni, altura)
    curs.execute("INSERT INTO Personas (Nombre, FechaNacimiento, Dni, Altura) values (?,?,?,?)", values)
    conn.commit()
    last_id = curs.lastrowid
    conn.close()
    return last_id

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
