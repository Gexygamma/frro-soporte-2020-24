# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.
def superposicion_loop(lista_1, lista_2):
    for elemento_a in lista_1:
        for elemento_b in lista_2:
            if elemento_a == elemento_b:
                return True
    return False


# se debe implementar utilizando conjuntos (sets).
def superposicion_set(lista_1, lista_2):
    return set(lista_1) & set(lista_2)

# extra: implementacion con generador.
def superposicion_gen(lista_1, lista_2):
    return any(item in lista_1 for item in lista_2)

assert superposicion_loop([1,3,5], [2,3,4])
assert not superposicion_loop([1,2,3], [4,5,6])
assert superposicion_set([1,3,5], [2,3,4])
assert not superposicion_set([1,2,3], [4,5,6])
assert superposicion_gen([1,3,5], [2,3,4])
assert not superposicion_gen([1,2,3], [4,5,6])