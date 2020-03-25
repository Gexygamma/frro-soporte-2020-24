# Implementar la función numeros_al_final(), que mueve todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.


# Resolver sin utilizar lista auxiliar
def numeros_al_final(lista):
    lista.sort(key = lambda n : type(n) == int)
    return lista

assert numeros_al_final([3,2,'b','a',1]) == ['b','a',3,2,1]
assert numeros_al_final(['f',6,'g']) == ['f','g',6]
