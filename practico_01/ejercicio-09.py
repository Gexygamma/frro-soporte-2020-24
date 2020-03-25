# Implementar la función es_palindromo(), que devuelva un booleano en base a
# si palabra se lee igual de corrido como al revés.
from math import ceil, floor

# Ejemplos: arenera, radar, ojo, oso, salas.
# Resolver sin utilizar loops (for/while), sino con slicing.
def es_palindromo(palabra):
    return palabra[:floor(len(palabra)/2)] == palabra[:ceil(len(palabra)/2)-1:-1]

assert es_palindromo("arenera")
assert es_palindromo("ojo")
assert not es_palindromo("palindromo")

