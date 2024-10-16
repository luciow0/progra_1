# En geometría un vector es un segmento de recta orientado que va desde un punto
# A hasta un punto B. Los vectores en el plano se representan mediante un par orde-
# nado de números reales (x, y) llamados componentes. Para representarlos basta
# con unir el origen de coordenadas con el punto indicado en sus componentes

# Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determi-
# narlo basta calcular su producto escalar y verificar si es igual a 0. 
# Ejemplo: 

# A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales

# Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor
# de verdad indicando si son ortogonales o no. Desarrollar también un programa que
# permita verificar el comportamiento de la función

def verificarOrtogonales(vectorUno, vectorDos):
    primerValorUno, primerValorDos = vectorUno
    segundoValorUno, segundoValorDos = vectorDos
    ortogonales = False
    if ((primerValorUno * segundoValorUno) + (primerValorDos * segundoValorDos)) == 0: 
        ortogonales = True

    return ortogonales

a = (2,3)
b = (-3,2)
hola = verificarOrtogonales(a,b)
if hola: 
    print("es ")
else: 
    print("no es ")