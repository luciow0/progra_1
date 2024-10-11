# Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas 
# son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True 
# o False. Escribir también un programa para verificar su comportamiento. Considerar 
# el uso de conjuntos para resolver este ejercicio.

# este ejercicio no se puede realizar con conjuntos ya que esta estructura de datos es desordenada 

def encajarDominos(dominoA, dominoB): 
    encajan = True
    conjuntoA = set()
    conjuntoB = set()
    for numero in dominoA:
        conjuntoA.add(dominoA)
    for numero in dominoB: 
        conjuntoB.add(dominoB)
    
    if conjuntoA.isdisjoint(conjuntoB):
        encajan = False
    
    return encajan

def ingresarNumeros(): 
    while True:
        try:
            num1 = int(input("Ingrese el primer numero de su domino "))
            break
        except ValueError: 
            print("Por favor ingrese un valor valido ")

    while True:
        try:
            num2 = int(input("Ingrese el segundo numero de su domino  "))
            break
        except ValueError: 
            print("Por favor ingrese un valor valido ")

    return num1, num2

def main():
    print("Ingrese los numeros de su primer domino")
    num1, num2 = ingresarNumeros()
    dominoA = num1, num2
    print("Ingrese los numeros de su primer domino") 
    num1, num2 = ingresarNumeros()
    dominoB = num1, num2

    verSiEncajan = encajarDominos(dominoA, dominoB)
    if verSiEncajan: 
        print("Dominos encajables")
    else: 
        print("Dominos no encajables")

main()
