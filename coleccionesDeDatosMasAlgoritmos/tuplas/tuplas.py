"""FUNCIONES Y OPERACIONES CON TUPLAS """

# una tupla es una estructura de datos INMUTABLE y ordenada 
# los datos se encierran entre parentesis, pueden ser de cualquir tipo y no necesitan ser todos del mismo tipo
# las tuplas tienen algunas funciones predefinidas como index(), len() y count(), ademas se pueden concatenar y repetir tuplas 
# con los operadores sobrecargador + y * respectivamente 
# tambien es posible acceder a sus elementos por medio de un indice entre [] 
# tambien se pueden extraer elementos usando slicing 
# cuando la tupla tiene solo un elemento se debe poner una coma anonima para que se considere como tal y no como un dato simple 
# las tuplas pueden o no estar dentro de parentesis 
# -
# una particularidad de las tuplas muy interesante sino la mas interesante es que se pueden empaquetar y desempaquetar, por ejemplo 

saludos = ('buenos dias', 'buenas noches', 'buenas tardes') #empaquetado
manana, noche, tarde = saludos #desempaquetado

# al desempaquetar, el numero de datos del lado izquierdo debe ser el mismo que de el derecho, sino dara error 
# se pueden convertir en tuplas otro tipo de datos con la funcion tuple(), por ejemplo 
letras = tuple("lagarto")
print(letras)

#se pueden concatenar tuplas 

fecha = ()
fecha += "Martes"

# las tuplas pueden compararse por medio de los opeardores relaciones, siempre y cuando tengan el mismo tipo de datos. y se sigue un criterio similar al de las cadenas 
