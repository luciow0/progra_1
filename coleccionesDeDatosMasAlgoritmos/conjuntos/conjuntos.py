## INICIO 

vocales = {'a','e','i','o','u'}
print("conjunto de vocales ", vocales)
print("tipo de dato ", type(vocales))
#las mostro como se le canto el orto digamos 

lista = [1,2,3,4,5,6,7,8,9,9]
tupla = (55,66,77,88,99,100,88)
cadena = "hola como andas"

setLista = set(lista) ## UNICO FORMATO EN EL QUE SET RESPETO EL ORDEN DE LOS ELEMENTOS, EN TODOS LOS OTROS LOS CAMBIO 
print(setLista)

setTupla = set(tupla)
print(setTupla)

setCadena = set(cadena)
print(setCadena, len(setCadena)) # TAMBIEN SE PUEDE MOSTRAR EL LEN DE LOS CONJUNTOS y por que no se podria wacho que onda q te pasa con los conjuntos 

#el len de un conjunto tambien se le dice su cardinalidad

#efectivamente no agrega elementos repetidos 

vacio = set()

print(vacio, type(vacio), len(vacio))

## operador de membresia 

if 66 in setTupla: 
    print("auuuuuuuuuu auu auauauau ")

if 120 not in setTupla: 
    print("guaaau")

"""---------------------------------------------------------------------------------------------------------------------------------------------------------"""

## FUNCIONES 

conjuntoUno = {"un conjunto aleatorio"}
conjuntoDos = {"Otro conjunto y que"}

elemento = "Un string para que python no me rompa las pelotas "

conjuntoUno.add(elemento) # agrega un elemento al conjunto, sin importar el orden. si este ya se encuentra dentro del conjunto, lo ignora 

conjuntoUno.update(conjuntoDos) #agrega al conjuntoUno todos los elementos del conjuntoDos

conjuntoUno.pop() # quita un elemento ALEATORIO del conjunto y lo regresa, si el conjunto esta vacio devuelve un keyError

# conjuntoUno.remove(elemento) # elimina el elemento especificado del conjunto, si este no pertenece genera un KEYERROR

conjuntoUno.discard(elemento) # elimina el elemento del conjunto y si este no pertenece, no genera un error
 
conjuntoUno.clear() # vacia el conjunto 

#############

conjuntoPrueba = {1,2,3}
conjuntoPruebaDos = {9,7,4,1}

conjuntoPrueba.add(11)
print(conjuntoPrueba)
conjuntoPrueba.add(11)
conjuntoPrueba.add(11)
print(conjuntoPrueba)
conjuntoPrueba.remove(11)
print(conjuntoPrueba)
conjuntoPrueba.pop()
print(conjuntoPrueba)
conjuntoPrueba.update(conjuntoPruebaDos)
print(conjuntoPrueba)
conjuntoPrueba.clear()
print(conjuntoPrueba)


"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

## OPERACIONES ENTRE CONJUNTOS 

# Entre las operaciones mas utilizadas de conjuntos se encuentran, la union, la interseccion, la diferecia, la diferencia simetrica 

# UNION: operacion binaria entre conjuntos da como resultado un tercer conjunto con los elementos de los dos conjuntos que participan en la operacion 

c1 = {1,2,3}
c2 = {4,5,6}
c3 = c1.union(c2)
print(c3)

# INTERSECCION: operacion binaria entre conjuntos cuyo resultado es un tercer conjunto con los elementos comunoes de los dos conjuntos que participan en la operacion 
# es decir, en el nuevo conjunto solo se incluiran aquellos elementos que esten presentes en ambos conjuntos 

c4 = {10,20,30}
c5 = {30,40,50}
c6 = c4.intersection(c5)
print(c6)

# DIFERENCIA: operacion binaria blabla con los ELEMENTOS DEL PRIMER CONJUNTO QUE NO ESTAN EN EL SEGUNDO 

c7 = {10,20,50}
c8 = {10,20,50}
c9 = c7.difference(c8) #c9 deberia ser vacio 
print(c9)

c10 = {"hola", "me", "llamo", "Juan"}
c11 = {"hola", "me", "llamo", "Lucio"}
c12 = c10.difference(c11)
print(c12)

# DIFERENCIA SIMETRICA DE CONJUNTOS: es una operacion blabla que el resultado son: LOS ELEMENTOS DEL PRIMER CONJUNTO QUE NO ESTAN EN EL SEGUNDO Y LOS ELEMENTOS DEL SEGUNDO CONJUNTO QUE NO ESTAN EN EL PRIMERO 

c13 = {1,7,9,5}
c14= {7,9,4,8,10}
c15 = c13.symmetric_difference(c14)
print(c15)


"""---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

# OPERACIONES LOGICAS ENTRE CONJUNTOS 

c1 == c2 # determina si el conjunto c1 es igual a c2: misma cardinalidad y elementos iguales sin importar el orden 

c1 != c2 # determina si c1  es distinto de c2, al menos un elemento diferente 

c1 <= c2 # determina si c1 es un subconjunto de c2, cada elemento de c1 esta en c2
c1.issubset(c2)

c1 >= c2 # determina si el conjunto c1 es un super conjunto de c2, cada elemento de c2 esta en c1 
c1.issuperset(c2)

c1 > c2 # detetmina si todos los elementos de c2 estan en c1, y ademas, c1 tiene otros elementos

c1 < c2 # determina si todos los elementos de c1 estan en c2, y ademas, c2 tiene otros elementos 

c1.isdisjoint(c2) # determina si c1 y c2 son conjuntos disjuntos, no tienen elementos en comun 

copia = c1.copy() # regresa una copia superficial del conjunto c1

"""
es importante destacar que los metodos de union, interseccion, diferencia y diferencia simetrica admiten mas de un parametro, 
en ese caso se separan por comas 
"""

"""--------------------------------------------------------------------------------------------------------------------------------------------"""

# Python, ofrece metodos que combinan update con interseccion, diferencia y diferencia simetrica, es decir 
# actualiza un conjunto con el resultado de la operacion que acompania al metodo update, en el caso de la union
# update hace exactamente eso, actuliza al conjunto que lo invoca con la union del conjunto como parametro 

c1.update(c2) #seria la union 
c1.intersection_update(c2)
c1.difference_update(c2)
c1.symmetric_difference_update(c2)


"""--------------------------------------------------------------------------------------------------------------------------------------------------------"""

# CONJUNTO FROZENSET 

# python ofrece una variable del tipo set para representar el concepto de conjunto. este tipo se conoce como frozenset y se diferencia 
# del anterior en que es INMUTABLE, es decir podriamos crear un conjunto inmutable. 
# para definir un conjunto de este tpo se utiliza el constructor frozenset y como parametro, cualquier dato iterable 

"""a partir de una cadena"""
vocales = frozenset('aeiou')
print(vocales)
print(type(vocales))

"""a partir de un conjunto"""
colores = frozenset({'rojo', 'verde', 'amarillo'})
print(colores)

"""a partir de una tupla"""
numeros = frozenset((1,2,3,4,5))
print(numeros)

# los conjuntos frozen tambien admiten las operaciones vistas con los set comunes, a excepcion de update y add ya que como son inmutables
# no se pueden actualizar, SE PUEDEN USAR: union interseccion y diferencia 
# tambien se pueden realizar estas operaciones entre: frozenset y set 
# el tipo de dato del resultado dependera del primer operando 
