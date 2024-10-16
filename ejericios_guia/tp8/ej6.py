# Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras
# repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras
# ordenadas según su longitud. Los signos de puntuación no deben afectar el
# proceso

def ingresarFrase():
    listaPalabras = []

    frase = input("Ingrese su frase ")
    frase = frase.split(" ")

    setLista = set(frase)

    listaPalabras = list(setLista)
    listaPalabras = ordenarLista(listaPalabras)

    print(listaPalabras)



def ordenarLista(lista): 
    for i in range(len(lista) -1):
        for j in range(len(lista) -1 -i):
            if len(lista[j]) < len(lista[j + 1]): 
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux 

    return lista

ingresarFrase()