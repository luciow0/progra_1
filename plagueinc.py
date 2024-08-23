import random
from time import sleep

def main():
    
    paises = [
        "Argentina", "Australia", "Brasil", "Canadá", "Chile",
        "China", "Colombia", "España", "Estados Unidos", "Francia",
        "India", "Italia", "Japón", "México", "Nigeria",
        "Noruega", "Países Bajos", "Perú", "Reino Unido", "Rusia",
        "Sudáfrica", "Suecia", "Suiza", "Turquía", "Venezuela"
    ]

########################################################################################

    #listas paralelas para trabajar con la lista principal (paises)
    poblacion = [random.randint(1000000,10000000)for _ in range(25)] #--> poblaciones correspondientes a cada pais, van a ser random en cada iteracion 
    vivos = [(0) for _ in range(25)]#sin uso por ahora
    infectados = [(1) for _ in range(25)]
    muertos = [(0) for _ in range(25)]#sin uso por ahora
    cura = [(0) for _ in range(25)]#sin uso por ahora
    Aproximacion = []

    # Generamos 25 tuplas, cada una con un rango de 10 números
    for i in range(25):
        start = i * 10 + 1
        end = start + 10
        tupla = tuple(range(start, end))
        Aproximacion.append(tupla)

    x = 0
    for j in range (10000): #bucle for maneja el tiempo de juego 
        
        probabilidadExpansion= [random.randint(1,1500)for _ in range(25)] #en cada iteracion, cada pais va a tener una probabilidad de expansion random
        for i in range(25):
            
            if infectados[i] < poblacion[i]: 
                infectados[i] += probabilidadExpansion[i]
                print("infectados ",infectados[i], "en ", paises[i],"\n")

            if x == 2:
                aux = probabilidadExpansion[i]
                infectados[i] -= (aux // 2)
                if infectados[i] < 1: 
                    infectados[i] = 0
                muertos[i] += (aux // 2)
                poblacion[i] -= (aux // 2)     
                if poblacion[i] < 1: 
                    poblacion[i] = 0  
                print("infectados ",infectados[i],"muertos ", muertos[i], "poblacion", poblacion[i], "en", paises[i])
                x = 1
            x += 1

print(" print final final infectados ",infectados[i],"muertos ", muertos[i], "poblacion", poblacion[i], "en", paises[i])

main()

#for i in range(10000):
#    
#    file = open("/home/luciowo/progra_1/planetaAscii.txt", 'r')
#    mostrar = file.read()
#    print(mostrar,"\n\n")
#    file.close()
#
#    file2 = open("/home/luciowo/progra_1/planetaAscii_2.txt", 'r')
#    mostrar2 = file2.read()
#    print(mostrar2,"\n\n")
#    file2.close()


