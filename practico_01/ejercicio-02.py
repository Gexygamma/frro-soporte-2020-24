# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.


def mayor(a, b, c):
    primer_par = a if a > b else b # mayor entre valores a y b
    return primer_par if primer_par > c else c

# si no falla es porque esta bien
assert mayor(1, 10, 5) == 10
assert mayor(4, 9, 18) == 18
