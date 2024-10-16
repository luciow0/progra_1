# Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
# usuario y eliminarlos del conjunto mediante el método remove, mostrando el con-
# tenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
# Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
# inexistentes.

def eliminarElementos(): 
    conjunto = {0,1,2,3,4,5,6,7,8,9}
    print("estado actual del conjunto ", conjunto)
    while True:
        try:

            numeroEliminar = int(input("Ingrese el numero que desea eliminar del conjunto "))

            break
        except ValueError: 
            print("Ingresa un entero flaco")

    while numeroEliminar != -1: 
        
        try: 
            conjunto.remove(numeroEliminar)
            print("estado actual del conjunto ", conjunto)
        except KeyError: 
            print("Ese numero ya ha sido eliminado del conjunto, por favor ingrese uno distinto ")
        
        finally: 
            while True:
                try:
                    numeroEliminar = int(input("Ingrese el numero que desea eliminar del conjunto "))
                    break
                except ValueError: 
                    print("Ingresa un entero flaco")

            

eliminarElementos()