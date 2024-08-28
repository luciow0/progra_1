import random
totalRecaudado = 0
matriz = []
filas = 5
columnas = 15
for f in range(filas): 
    matriz.append([])
    for c in range(columnas): 
        matriz[f].append(" ")

#print(matriz)

#for i in range(5): 
#    for j in range(15): 
#        aux = random.randint(0,1)
#        if aux == 1: 
#            totalRecaudado += 10000
#            matriz[i][j] = ('X')
        
#for i in range(5):
#    print('PISO', i)
#    for j in range(15):
#        print('DPTO',j, matriz[i][j], end=" ")
#    print( )


piso = int(input("Ingrese el numero de piso entre 1 y 5, 99 para finalizar "))
while piso != 99: 
    if piso < 1 or piso > 5:
        piso = int(input("Ingrese el numero de piso entre 1 y 5, 99 para finalizar "))
    for i in range(15): 
        print("Pago el depto",i+1, "las expensas? ")
        pago = int(input("ingrese 1 para si 0 para no "))
        while pago != 1 and pago != 0:
            pago = int(input("ingrese 1 para si 0 para no aaa "))
        if pago == '1': 
            matriz[piso][i] = 'X'
            totalRecaudado += 10000
     
for i in range(5):
    print('PISO', i)
    for j in range(15):
        print('DPTO',j, matriz[i][j], end=" ")
    print( )
        