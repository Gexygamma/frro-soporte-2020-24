# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3 as sql

def crear_conexion():
    conn = sql.connect("base_datos.db")
    return conn, conn.cursor()

def crear_tabla():
    conn, curs = crear_conexion()
    curs.execute("""CREATE TABLE IF NOT EXISTS Personas (
        IdPersona INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT,
        FechaNacimiento TEXT,
        Dni INTEGER,
        Altura INTEGER
    ) """)
    conn.commit()
    conn.close()

def borrar_tabla():
    conn, curs = crear_conexion()
    curs.execute("DROP TABLE IF EXISTS Personas")
    conn.commit()
    conn.close()

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
