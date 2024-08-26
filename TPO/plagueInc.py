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
    paisesSinPoblacion = []
    vivos = [(0) for _ in range(25)]
    muertosPorPais = [(0) for _ in range(25)]
    cura = [(0) for _ in range(25)]
    infectados = [(1) for _ in range(25)]
    poblacion = [random.randint(1000000,10000000)for _ in range(25)]
    infectadostotales = 0
    filas = 25
    columnas = 9120
    matrizProximosMuertos = []
    for i in range(filas): 
        matrizProximosMuertos.append([0] * columnas)

   
    x = 0
    for j in range (9120):
          
   
        for i in range(25):
            probabilidadExpansion= [random.randint(300,550)for _ in range(25)]
            if infectados[i] < poblacion[i]: 
                infectados[i] += probabilidadExpansion[i]
                infectadostotales += probabilidadExpansion[i]
                matrizProximosMuertos[i][j] = infectados[i]
                #print(matrizProximosMuertos)
                #print("infectados ",infectados[i], "en ", paises[i],"\n")

            else:
                if paises[i] not in paisesSinPoblacion:
                    paisesSinPoblacion.append(paises[i])

            if x == 5:
                for o in range(25):
                    muertosPorPais[o] = matrizProximosMuertos[o-5][o-5]
                    infectados[i] -= (muertosPorPais[i])
                    poblacion[i] -= (muertosPorPais[i])       
                #print("infectados ",infectados[i],"muertos ", muertos[i], "poblacion", poblacion[i], "en", paises[i])
                x = 0
                
        x += 1    
          
    print("MUERTOS POR PAIS ", muertosPorPais, "paises sin poblacion ", paisesSinPoblacion)


main()

#for i in range(10000):
    
#   file = open("/home/luciowo/progra_1/planetaAscii.txt", 'r')
#    mostrar = file.read()
#    print(mostrar,"\n\n")
#    file.close()

#    file2 = open("/home/luciowo/progra_1/planetaAscii_2.txt", 'r')
#    mostrar2 = file2.read()
#    print(mostrar2,"\n\n")
#    file2.close()