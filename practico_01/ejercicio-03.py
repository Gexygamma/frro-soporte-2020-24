# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".


def operacion(a, b, multiplicar):
    if multiplicar:
        return a * b
    elif b != 0:
        return a / b
    else:
        print('Operación no válida.')
        # raise ZeroDivisionError

assert operacion(2, 3, True) == 6
assert operacion(8, 2, False) == 4