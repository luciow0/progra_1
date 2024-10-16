"""
Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves
"""

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


diccionarioCuadrados = dict([(n, n ** 2) for n in lista])

print(diccionarioCuadrados)

