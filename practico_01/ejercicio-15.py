# Reescribe el programa que pide al usuario una lista de números e imprime en
# pantalla el máximo y mínimo de los números introducidos al final,cuando el usuario
# introduce “fin”. Escribe ahora el programa de modo que almacene los números que
# el usuario introduzca en una lista y usa las funciones Max () y min () para calcular los
# números máximo y mínimo después de que el bucle termine.

print("Escriba 'fin' para terminar el ingreso de datos.")
paso = 1
lista = []
while True:
    ingreso = input("Ingrese el número {}: ".format(paso))
    if ingreso.lower() != 'fin':
        try:
            numero = int(ingreso)
        except ValueError:
            print("Ingreso con formato incorrecto. Intente nuevamente.")
        else:
            paso += 1
            lista.append(numero)
    else:
        break
print("El máximo es {}".format(max(lista)))
print("El mínimo es {}".format(min(lista)))