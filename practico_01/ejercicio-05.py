# Implementar la función es_vocal, que reciba un carácter y
# devuelva un booleano en base a si letra es una vocal o no.


# Resolver utilizando listas y el operador in.
vocales = "aeiou"

def es_vocal(letra):
    return letra in vocales

assert es_vocal('e')
assert not es_vocal('b')