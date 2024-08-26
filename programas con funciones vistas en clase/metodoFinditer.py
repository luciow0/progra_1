import re

texto = "Los correos de contacto son oliver@dominio.com y  gabriela@dominio.com."

patron = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

iteradorCorreos = re.finditer(patron, texto)

#Iteramos sobre el iterador para mostrar información detallada de  cada correo encontrado​

print("Información detallada de correos electrónicos  encontrados:")

for match in iteradorCorreos:

    print(f"Correo electrónico encontrado: {match.group()}") 
    print(f"Ubicación: inicio={match.start()}, fin={match.end()}")  
    print("----")