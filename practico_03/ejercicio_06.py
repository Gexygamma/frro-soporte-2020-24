# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from ejercicio_01 import crear_conexion, borrar_tabla, crear_tabla

def crear_tabla_peso():
    conn, curs = crear_conexion()
    curs.execute("""CREATE TABLE IF NOT EXISTS PersonaPeso (
        IdPersona INTEGER,
        Fecha TEXT,
        Peso INTEGER,
        PRIMARY KEY(IdPersona, Fecha),
        FOREIGN KEY(IdPersona) REFERENCES Personas(IdPersona)
    ) """)
    conn.commit()
    conn.close()

def borrar_tabla_peso():
    conn, curs = crear_conexion()
    curs.execute("DROP TABLE IF EXISTS PersonaPeso")
    conn.commit()
    conn.close()

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
