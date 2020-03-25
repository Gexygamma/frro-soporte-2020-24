# Implementar la función multiplicar() que devuelva el producto de todos los números de una lista.


# [1,2,3,4] -> 24
def multiplicar(lista):
    if lista: # si la lista no esta vacia
        resultado = lista[0]
        for elemento in lista[1:]: # recorro la lista a partir del elemento 1
            resultado *= elemento
    else:
        resultado = 0
    return resultado

assert multiplicar([1,2,3,4]) == 24
assert multiplicar([]) == 0
assert multiplicar([2]) == 2
