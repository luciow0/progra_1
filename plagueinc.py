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

    poblacion = [random.randint(1000000,10000000)for _ in range(25)]
    vivos = [(0) for _ in range(25)]
    infectados = [(1) for _ in range(25)]
    muertos = [(0) for _ in range(25)]
    cura = [(0) for _ in range(25)]
    
    #rangos = [random.randint(25,50)for _ in range(25)]

    #rangos = [
    #(1,25),(1,24),(1,23),(1,22),(1,21),(1,21),
    #(1,19),(1,18),(1,17),(1,16),(1,15),(1,14),(1,13),
    #(1,12),(1,11),(1,11),(1,19),(1,18),(1,17),(1,16),(1,15),
    #(1,14),(1,13),(1,13),(1,11)
    #]

    x = 0
    for j in range (10000):
        
        probabilidadExpansion= [random.randint(300,550)for _ in range(25)]
        for i in range(25):
            
            if infectados[i] < poblacion[i]: 
                infectados[i] += probabilidadExpansion[i]
                print("infectados ",infectados[i], "en ", paises[i],"\n")
            if x == 2:
                aux = probabilidadExpansion[i]
                infectados[i] -= (aux // 2)
                muertos[i] += (aux // 2)
                poblacion[i] -= (aux // 2)       
                print("infectados ",infectados[i],"muertos ", muertos[i], "poblacion", poblacion[i], "en", paises[i])
                x = 1
            x += 1


#main()

for i in range(10000):
    
    file = open("/home/luciowo/progra_1/planetaAscii.txt", 'r')
    mostrar = file.read()
    print(mostrar,"\n\n")
    file.close()

    file2 = open("/home/luciowo/progra_1/planetaAscii_2.txt", 'r')
    mostrar2 = file2.read()
    print(mostrar2,"\n\n")
    file2.close()