"""
Escribir un programa que permita ingresar un número entero N y genere un
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la
tabla de multiplicar con el formato apropiado
"""

def generarDiccionario(): 
    try: 
        tabla = int(input("Ingrse el numero de el cual desea realizar la tabla "))

    except ValueError: 
        print("Debias ingresar un entero ")

    listaTuplas = []
    for i in range(1,13): 
        producto = tabla * i
        tupla = (f"{tabla} x {i} = ", producto)
        listaTuplas.append(tupla)

    diccionarioTablas = dict(listaTuplas)
    print(diccionarioTablas)


generarDiccionario()

