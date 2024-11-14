""" 
Realizar la implementación recursiva del método de selección para ordenar una lista
de números enteros. Sugerencia: Colocar el elemento más pequeño en la primera
posición, y luego ordenar el resto de la lista con una llamada recursiva. No usar las
funciones min() ni max() de Python
"""
"""
def ord_seleccion(arreglo):
    for i in range(len(arreglo) - 1):        # <-- bucle padre
        menor = i # primer elemento por default será el mínimo

        for j in range(i + 1, len(arreglo)): # <-- bucle hijo
            if arreglo[j] < arreglo[menor]:
                menor = j

        if menor != i:
            arreglo[menor], arreglo[i] = arreglo[i], arreglo[menor]

a = [22, 25, 12, 64, 11]
ord_seleccion(a)

print(a)
"""
def sumar(lista):
    if len(lista) == 0:
        return suma
    else:
        return suma + lista[0] sumar(lista[1:])