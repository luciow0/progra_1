#matriz de prueba
matriz = [
    ["perro",0,0,0],
    ["gato",0,0,0],
    [0,0,0,0]
]
#funcion A
def cargarNumerosEnterosMatriz(matriz): 
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas): 
        for c in range(columnas): 
            n = int(input("Ingrese el entero que desea agregar a la lista"))
            while n < 1: 
                n = int(input("Ingrese el entero que desea agregar a la lista"))
            matriz[f][c] = n

#funcion B preguntar 

#funcion C
def intercambiarDosFilas(matriz,filaA, filaB):
     aux = matriz[filaA]
     matriz[filaA] = matriz[filaB]
     matriz[filaB] = aux
     print(matriz)


#funcion D
def intercambiarDosColumnas(matriz,columna1,columna2): 
    filas = len(matriz)
    for f in filas: 
        aux = matriz[f][columna2]
        matriz[f][columna2] = matriz[f][columna1]
        matriz[f][columna1] = aux
    
    print(matriz)

intercambiarDosColumnas(n)