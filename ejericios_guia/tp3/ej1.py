#matriz de prueba
matriz = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
]

#matriz desordenada de prueba
matrizDesordenada = [
    [5,2,6,1],
    [9,7,5,3],
    [1,5,3,6],
    [8,1,9,2]
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

#funcion B, ordenando de forma ascendente fila a fila
def ordenarMatrizAscendente(matriz): 
    filas = len(matriz)
    for f in range(filas): 
        matriz[f].sort()
    
    mostrarMatriz(matriz)

#funcion C
def intercambiarDosFilas(matriz,filaA, filaB):
     aux = matriz[filaA]
     matriz[filaA] = matriz[filaB]
     matriz[filaB] = aux
     print(matriz)


#funcion D
def intercambiarDosColumnas(matriz,columna1,columna2): 
    filas = len(matriz)
    for f in range(filas): 
        aux = matriz[f][columna2]
        matriz[f][columna2] = matriz[f][columna1]
        matriz[f][columna1] = aux
    
    mostrarMatriz(matriz)

#funcion mostrar
def mostrarMatriz(matriz): 
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):  
            print(matriz[f][c], end = " ")
        print()

#funcion copiar
def copiarMatrices(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matrizDos = [] 
    for f in range(filas): 
        fila = []
        for c in range(columnas): 
            fila.append(matriz[f][c])
        matrizDos.append(fila)
    return matrizDos

#funion e, debe recibir si o si una matriz nxn para no dar error, #millones o incluso, miles de millones 
def trasponerMatriz(matriz): 
    filas = len(matriz)
    columnas = len(matriz[0])
    matrizCopia = copiarMatrices(matriz)
    for f in range(filas): 
        for c in range(columnas): 
            if matriz[f][c] != matrizCopia[f][c]: 
                continue
            else: 
                aux = matriz[f][c] 
                matriz[f][c] = matriz[c][f]
                matriz[c][f] = aux
    mostrarMatriz(matriz)

#funcion f, calcular el promedio de los elementos de una fila 
def calcularPromFila(matriz,fila): 
    filas = len(matriz)
    columnas = len(matriz[0])
    sumador = 0
    for c in range(columnas): 
        sumador += matriz[fila][c]
    promedio = sumador / filas
    print("El promedio de la fila ",fila,"es ", promedio)

#funcion g, calcular el porcentaje de elementos impares en una columna
def calcularPorcImp(matriz,columna): 
    pares = 0 
    impares = 0
    filas = len(matriz)
    for f in range(filas):
        if matriz[f][columna] % 2 != 0: 
            impares += 1
        else: 
            pares += 1
    porcImpares = impares * (pares + impares) / 100
    print(porcImpares)

#funcion h, matriz simetrica con respecto a su diagonal principal 