#Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
#para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
#cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
#caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
#de alguna naranja se encuentra fuera del rango indicado se la clasifica para
#rocesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas
#cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
#ugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
#reparto. Simular el peso de cada unidad generando un número entero al azar entre
#50 y 350.
#Además, se desea saber cuántos camiones se necesitan para transportar la cose-
#cha, considerando que la ocupación del camión no debe ser inferior al 80%; en
#caso contrario el camión no serán despachado por su alto costo
import random

def cargarNaranjas(cantidad):
    naranjasJugo = []
    naranjasCajon = []
    cajonesDeNaranja = []
    contador = 0
    while j < cantidad:
        naranjasAux = random.randint(150,350)
        if naranjasAux < 200 or naranjasAux > 300: 
            naranjasJugo[j].append(naranjasAux)
        else:
            if contador <= 100: 
                naranjasCajon[j].append(naranjasAux)
                contador += 1
            else:
                contador = 0

        j += 1

        print("")

for i in range() : 

    for j in range(): 

        if contador <= 100: 
                naranjasCajon[i] += naranjasAux
                cajonesDeNaranja
                contador += 1
        else:
            contador = 0