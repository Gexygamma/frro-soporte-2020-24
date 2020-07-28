# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

from ejercicio_01 import crear_conexion, reset_tabla
from ejercicio_02 import agregar_persona

def buscar_persona(id_persona):
    conn, curs = crear_conexion()
    values = (id_persona, )
    result = curs.execute("""SELECT IdPersona, Nombre, FechaNacimiento, DNI, Altura
        FROM Personas WHERE IdPersona = ?""", values)
    row = result.fetchone()
    conn.close()
    if row is None:
        return False
    _id, nombre, nacimiento_str, dni, altura = row
    nacimiento = datetime.datetime.strptime(nacimiento_str[:10], '%Y-%m-%d')
    return _id, nombre, nacimiento, dni, altura

@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
