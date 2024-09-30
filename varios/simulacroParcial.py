"""
Conocimientos necesarios: funciones, listas, matrices, strings.
SOLO RESUELVA CON EL ALCANCE DE LOS CONTENIDOS TRABAJADOS EN CLASE

1) Una fábrica de luminarias, produce 100 modelos distintos de artefactos. 
Los modelos están codificados con códigos de 3 cifras, sin repeticiones. 
Utilizar una FUNCIÓN para ingresar los códigos de los modelos validados.
Para cada modelo hay 3 opciones de artefactos según el uso: 
1- Interior 
2- Alumbrado Público 
3- Profesional y grandes superficies.

Diariamente, al finalizar la producción, se ingresan por teclado los siguientes datos:
- Código del MODELO (3 cifras)
- Código de uso (1 a 3) - Utilizar FUNCION para leer y controlar
- Cantidad producida (número entero y positivo)
Esta información termina con Código de Modelo -10
Si el código del modelo NO existe, indicar “CODIGO ERRONEO” en el programa principal. 
Utilizar función BusquedaMod

SE PIDE INFORMAR:
a) Un listado donde indique cantidad producida según código de modelo y el uso, con el siguiente formato.
 
#ver en diapositiva
Utilizar para el informe utilizar la función ListadoCantidad.

b) Un listado ordenado en forma ascendente por cantidad confeccionada por uso, indicando
CANTIDAD PRODUCIDA POR TIPO USO
USO                  CANTIDAD

c) Indicar los modelos que NO fueron producidos para ningún uso.

2) (VALOR 3 PUNTOS) Ejercicio: Crear un módulo de validación de nombre de usuario. 
Debe cumplir con las características:
• Longitud mayor a 6 caracteres y menor a 12
• Debe ser alfanumérico

Datos de entrada:
• Nombre de usuario

Proceso:
• Validar si es mayor a 6 caracteres y menor a 12
• validar si alfanumérico

Datos de Salida:
1) Retornar un mensaje si es mayor a 6 caracteres
2) Imprimir un error si es menor a 6 caracteres
3) Retornar mensaje de error si no es alfanumérico
4) Imprimir mensaje de bienvenida y concatenado con el nombre de usuario
3) (VALOR 2 PUNTOS) Utilizar la técnica de listas por comprensión para construir una lista con todos los
números impares comprendidos entre 100 y 200
"""

import random 

def generarModelosRandom(): 
    modelos = []
    artefactos = []
    while len(modelos) < 100: 
        aux = random.randint(100,999)
        if aux not in modelos: 
            modelos.append(aux)
        aux = random.randint(1,3)
        artefactos.append(aux)

    print(modelos)
    print()
    print(artefactos)

def busquedaMod(modelo):
    pass

# ya entendi  

def cargarCantidadDeModelos(): 
    
    codigoDeModelo = int(input("Ingrese el codigo de modelo de producto que desea cargar"))
    #while codigoDeModelo

generarModelosRandom()