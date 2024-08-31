import random
#no tengo ni la menor idea de como hacer esto 
def normalizarLista(lista): 
    for i in range(len(lista)-1): 
        aux = lista[i] / len(lista)
        lista[i] = aux
    return lista

