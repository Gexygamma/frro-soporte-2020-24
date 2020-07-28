# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime

from ejercicio_01 import crear_conexion
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona
from ejercicio_06 import reset_tabla

def agregar_peso(id_persona, fecha, peso):
    conn, curs = crear_conexion()
    # Validar que existe la persona.
    if not buscar_persona(id_persona):
        return False
    # Validar que no existe registro posterior.
    values = (id_persona, )
    result = curs.execute("SELECT Fecha FROM PersonaPeso WHERE IdPersona = ?", values)
    for fecha_result, in result.fetchall():
        if datetime.datetime.strptime(fecha_result[:10], "%Y-%m-%d") >= fecha:
            return False
    # Insertar nuevo registro.
    values = (id_persona, fecha, peso)
    curs.execute("INSERT INTO PersonaPeso (IdPersona, Fecha, Peso) values (?,?,?)", values)
    conn.commit()
    last_id = curs.lastrowid
    conn.close()
    return last_id

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
