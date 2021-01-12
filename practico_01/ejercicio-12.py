# Determinar la suma de todos los numeros de 1 a N. N es un número que se ingresa
# por consola.

n = int(input("Ingrese un número: "))

suma = 0
for i in range(1, n+1):
    suma += i

print("La suma de todos los números del 1 al {} es {}".format(n, suma))