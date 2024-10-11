# realizar un programa para ingresar una frase y mostrar un listado ordenado 
# alfabeticamente con las palabras que contiene, eliminando las repetidas y aniadiendo 
# junto a cada una la cantidad de veces que se encontro 

def ingresarPalabras(frase): 
    frases = frase.split(" ")
    diccionario = {}
    for palabra in frases: 
        palabra = palabra.upper()
        if palabra in diccionario:
            clave = palabra
            diccionario[clave] += 1
        else: 
            clave = palabra
            diccionario[clave] = 1

    print(diccionario)

frase = "hola que tal hola que tal sisi ayer me comi una pizza de ugis bien piola la verdad que me zarpe comiendomela toda pero estaba goood"
ingresarPalabras(frase)
