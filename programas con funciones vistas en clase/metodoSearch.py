import re 

cadena = "El precio del producto es $11.33."

patron = '[0-9]+'

match = re.search(patron, cadena)  

if match: 

    numeroEncontrado = match.group()  
    posicionInicio = match.start()  
    posicionFin = match.end()
    posicionSpan = match.span()  #Tupla con (inicio, fin)​

    print(f"Primer número encontrado: {numeroEncontrado}")  
    print(f"Posición donde comienza: {posicionInicio}")  
    print(f"Posición donde termina: {posicionFin}")  
    print(f"Posición donde comienza y termina (tupla span):{posicionSpan}")

else:

    print("No se encontró ningún número en la cadena.")

#Search insensible a mayusculas 

cadena = "Morty, a veces la Ciencia es más arte que Ciencia..."

patron = 'ciencia'

match = re.search(patron, cadena, re.IGNORECASE)


if match:
    print(f"Se encontró '{match.group()}' en la posición {match.start()}.")
else:
    print("No se encontró ninguna coincidencia.")