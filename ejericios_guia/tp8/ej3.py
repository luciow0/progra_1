# Desarrollar un programa que utilice una función que reciba como parámetro una
# cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
# una tupla con las distintas partes que componen dicha dirección. Ejemplo:
# alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
# formatos de email inválidos y devolver una tupla vacía.

def cortarCorreo(email):

    if "@" not in email:
        emailPartido = ()
    elif "." not in email:
        emailPartido = ()
    else:    
        if email.count(".") == 2:
            partes = email.split("@")
            nombre, direccion = partes
            partesDireccion = direccion.split(".")
            dominio, com, ar = partesDireccion
            emailPartido = nombre, dominio, com, ar
        elif email.count(".") == 1:
            partes = email.split("@")
            nombre, direccion = partes
            partesDireccion = direccion.split(".")
            dominio, com = partesDireccion
            emailPartido = nombre, dominio, com
            

    return emailPartido

def main(): 
    print("Ingrese su direccion de correo electronico ")
    direccion = input(" ")
    emailPartido = cortarCorreo(direccion)
    while emailPartido == ():
        print("Por favor ingrese una direccion de correo electronico valida ")
        direccion = input(" ")
        emailPartido = cortarCorreo(direccion)
        
    else: 
        print("email partido: ",emailPartido)

main()
