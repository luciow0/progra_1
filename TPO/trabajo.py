import random

#def imprimirMatriz(matriz): 
    #autodectamos el tamaño de la matriz 
#    filas = len(matriz)
#    columnas = len(matriz[0])
#    for f in range (filas): 
#        for c in range(columnas): 
#            print(matriz[f][c], end=" ")
#        print()

def inicializarListas(listaHabitantes,infectados): 
    filas = 23
    columnas = 3
    matriz = [[0] * columnas for i in range(filas)] #se preinicializa la matriz por comprension con valores en 0 para luego ser remplazados
    #el siguiente bucle for, accede directamente a las 3 posiciones (columnas) de la matriz 
    #de sanos, infectados y muertos, correspondientemente y recorre pais por pais asignando sus valores random de p
    #
    for f in range(filas):
        matriz[f][0] = (listaHabitantes[f] - infectados[f]) #sanos 
        matriz[f][1] = infectados[f] #infectados 
        matriz[f][2] = 0 #muertos
    imprimirMatriz(matriz)

listaHabitantes = [(random.randint(100000,1000000)) for _ in range(23)]
infectados = [(random.randint(100,1000)) for _ in range(23)]

inicializarListas(listaHabitantes,infectados)
