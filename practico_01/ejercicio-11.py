# Implementar la función es_primo(), que devuelva un booleano en base a
# si numero es primo o no.


def es_primo(numero):
    return not any(numero % n == 0 for n in range(2,numero)) and numero > 1

assert es_primo(7)
assert es_primo(13)
assert not es_primo(1)
assert not es_primo(15)
