# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.


def mayor(*args):
    return max(args)

# si no falla es porque esta bien
assert mayor(1, 10, 5) == 10
assert mayor(4, 9, 18) == 18
