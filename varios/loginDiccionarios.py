

def validarUsuarioContrasenia(usuario, contrasenia, diccionarioLogis): 
    valido = False
    for usuario in diccionarioLogis: 
        if contrasenia == diccionarioLogis[usuario]: 
            valido = True

    return valido


def registrarUsuarioContrasenia(usuario,contrasenia): 

    pass

def verificarExistencia(usuario, diccionario):
    existe = False
    if usuario in diccionario: 
        existe = True
    return existe

def login():

    diccionarioLogis = {'juan':'juan123'}

    print("Bienvenido, si ya posee una cuenta escriba 'Login', si no posee una escriba 'Registro' (case insensitive) ")
    ingreso = input(" ")
    ingreso = ingreso.upper()
    while ingreso != "LOGIN" and ingreso != 'REGISTRO': 
        print("Por favor ingrese una opcion valida ")
        ingreso = input(" ")
    
    if ingreso == "LOGIN": 
        valido = False
        while valido == False:         
            print("Ingrese su usuario y contrasenia ")
            usuario = input("Usuario: ")
            contrasenia = input("Contrasenia: ")
            valido = validarUsuarioContrasenia(usuario, contrasenia, diccionarioLogis)
        else: 
            print("Felicitaciones, te logueaste con exito")

    else: 
        print("Ingrese su nombre de usuario con el que desea registrarse ")
        usuario = input(" ")
        existe = verificarExistencia(usuario, diccionarioLogis)
        while existe: 
            print("Nombre de usuario en uso, por favor ingresa uno distinto")
            usuario = input(" ")
            existe = verificarExistencia(usuario, diccionarioLogis)
        else: 
            print("Ingrese la contrasenia con la que desea logearse ")
            contrasenia = input(" ")
            print("Repita la contrasenia ingresada ")
            contraseniaCheck = input(" ")
            while contrasenia != contraseniaCheck: 
                print("Error, escriba dos veces la misma contrasenia ")

login()