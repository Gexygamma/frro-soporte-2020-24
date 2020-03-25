# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.
from math import ceil

# hola -> ho
# verde -> ver
def mitad(palabra):
    return palabra[:ceil(len(palabra)/2)]

assert mitad("hola") == "ho"
assert mitad("verde") == "ver"