# Desarrollar un programa que utilice una función que reciba como parámetro una
# cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
# una tupla con las distintas partes que componen dicha dirección. Ejemplo:
# alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
# formatos de email inválidos y devolver una tupla vacía.

#def cortarCorreo(email):

email = "lclaa@uade.edu.ar"
partes = email.split("@")
nombre, direccion = partes
partesDireccion = direccion.split(".")
#es por ahi paa
print(partes)
print(nombre, direccion, partesDireccion)