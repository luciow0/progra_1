def pais():
    pais = "Argentina"  
    probabilidadExpansion = (random.randint(1,1500))
    progresoCura = 0
    avanceCura = (random.randint(1,10))
    poblacion = random.randint(1000000, 10000000)

    if infectados[i] < poblacion[i]: 
        infectados[i] += probabilidadExpansion[i]
        print("infectados ",infectados[i], "en ", paises[i],"\n")
    

    if x == 2: 
        progresoCura += avanceCura
        x = 1
    x += 1
    if progresoCura == 100: 
        