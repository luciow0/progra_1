"""en python los diccionarios son de tipo dict y se declaran de la siguiente manera """

# diccionario = {clave1: valor1, clave2: valor2}

# cada item o elemento tiene una forma clave: valor 
# en cada item hay una clave y uno o mas valores, si por alguna razon se desconoce el valor se puede completar con none 
# los elementosde un diccionario se indexan por la clave 
# las claves solo pueden ser datos inmutables 
# los valroes pueden ser datos mutables o inmutables
# las claves no pueden repetirse dentro de un diccionario 

"""
para comprobar si un objeto puede o no ser la clave de un diccionario se utiliza la funcion 
hash(objeto) que regresa el valor hash del objeto si lo tiene, por ejemplo la funcion hash(1) regresa 1 
mientras que, la funcion hash(lista) regresa un typerror por que las listas no son 'hasheables'

"""

# FUNCION FROMKEYS 
# se crea un diccionario en el cual las claves de sus items seran cada uno de los elementos de las secuencias 
# y los valores seran todos iguales al segundo parametro 

lista = [1,2,3,4,543,543,543,6124,32,432,13]
diccionarioFromKeys = dict.fromkeys(lista, "valor que tendra esto")
print(diccionarioFromKeys)

"""
los diccionarios tambien pueden crearse por medio del metodo constructor 'dict', 
"""

# por medio de una lista de tuplas 
dic1 = dict([('la paz', 13), ('lima', 15), ('villa luzuriaga', 77), ('villa elisa', 90)])
print(dic1, type(dic1))

# por medio de una lista por compresion
dpares = dict([(n, n **3) for n in range(1,5)])
print(dpares)

# usando parametros de palabras clave 
dic2 = dict(juan = 5324324, irene = 523432432)
print(dic2)

# por medio de un diccionario 
dic3 = dict({'irene': 312, 'vicky': 312, 'yo': 1000})
print(dic3)

"""-----------------------------------------------------------------------------------------------------------------------------------------"""

# OPERACIONES CON DICCIONARIOS 

"""AGREGAR ELEMENTOS"""

dic = {'clave'}

# Agregar elementos 
# dic['clave nuevo elemento'] = 500 #valor del nuevo elemento 
#si la clave ya existe en el diccionario, la instruccion cambia el valor asociado a la clave 

# otra forma de agregar elementos es con el medoto .update() 
# con este metodo se agregan los elementos de un diccionario a otro diccionario, solo si las claves no estan en el diccionario 
# por otro lado, si algunas de las claves estuvieran en el diccionario, entonces solo se modifican los valores correspondientes a dichas claves 

diccionarioUpdatear = {'clave1': "sarandeando la maracatunga aca un ratito", 'clave2': 10, 'clave3': 'valor3', 'clave4': 'chorizo mojado en cafe', 'clave5': 'valor5'}
diccionarioUpdateador = {'clavel1': 22, 'clavel2': 'valor1', 'clave3': 'MONDONGO', 'clavel4': 'MONDONGO', }

diccionarioUpdatear.update(diccionarioUpdateador)
print(diccionarioUpdatear)
# se modifico la clave 4 y se agregaron las otras 

"""CONSULTAR O MODIFICAR ELEMENTOS"""

# los valores se pueden consultar o modificar por medio de la clave 
print(diccionarioUpdatear['clave1']) #para acceder a un valor de un diccionario es por medio de la clave 

print(diccionarioUpdatear['clave2'])
diccionarioUpdatear['clave2'] += 10 #modifica el valor de la clave2 
print(diccionarioUpdatear['clave2'])

#usando get como en java 
print(diccionarioUpdatear.get('clave4'))

"""ELIMINAR ELEMENTOS"""

# hay mas de una manera de eliminar elementos de un diccionario 
# la instruccion 'del' elimina un par por su clave
# pop(clave) elimina el elemento cuya clave se proporciona y regresa el valor de este 
# popitem() elimina arbitrariamente un item y lo retorna ¿por que querrias hacer eso? 
# clear() vacia el diccionario

"""OPERADOR DE MEMBRESIA"""

# los operadores de membresia in y not in se pueden usar solo con claves, estos determinan si una clave esta o no en un diccionario 
# dando el valor de true o de false correspondientemente
# SI SE USA CON VALORES, NO DA ERROR, DARA SIEMPRE FALSE

"""FUNCIONES PREDEFINIDAS Y COMPARACION DE DICCIONARIOS"""

len(dic) # regresa el total de items del diccionario 
all(dic) # evalua si todas las claves tienen valor True, para que un valor sea true no puede ser 0, Flase, None, una cadena o una tupla vacia
any(dic) # evalua si alguna de las claves tiene valor True
sorted(dic) # genera una lista de claves ordenadas de menor a mayor. para cambiar el orden, se debe usar el parametro REVERSE,
            # ademas, si se desea que el diccionario se ordene por el valor, a la funcion sorted() se le debe dar el parametro key

# por el lado de la comparacion de diccionarios (==) y (!=), 
# para que dos diccionarios sean iguales deben tener la misma cantidad de elementos y los mismos elementos, sin importar el orden

"""ITERACION SOBRE DICCIONARIOS"""

# para iterar sobre un diccionario se pude utilizar el ciclo for para recorrer todos sus elementos
# hay que tener en cuenta que de esta forma se itera sobre las claves

menu = {'helado': 20, 'salchicha': 45, 'raviol': 99, "mandarina": 100000000000}
for comida in menu: 
    print(menu[comida])

# se itera sobre la clave y se muestra el valor 

"""METODOS KEYS() VALUES() E ITEMS()"""
