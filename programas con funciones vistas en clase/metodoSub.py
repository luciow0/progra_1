# Se utiliza para reemplazar todas las  ocurrencias de un patrón de expresión regular  en una cadena de texto con otra cadena  especificada.​

import re

texto = "El número de teléfono de Oliver es 123-456-7890, y el de Gabriela es 987-654-3210."

patron = "[0-9]{3}-[0-9]{3}-[0-9]{4}"

cadenaEnmascarada = "XXX-XXX-XXXX"

#Utilizamos re.sub() para reemplazar todos los números de​ teléfono por la cadena enmascarada

textoOfuscado = re.sub(patron, cadenaEnmascarada, texto)

print("Texto original:")  

print(texto)

print("\nTexto después de ofuscar los números de teléfono:")

print(textoOfuscado)