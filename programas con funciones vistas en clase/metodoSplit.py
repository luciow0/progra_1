# A diferencia del método split convencional de  Python, que solo admite cadenas simples  como delimitadores, 
# re.split permite utilizar  patrones más complejos basados en  expresiones regulares para separar la cadena  en partes más significativas.​

import re

texto = "Hola, ¿cómo estás? Espero que bien. Yo estoy bien  también."

#Este patrón divide por cualquier combinación de puntos, comas,  signos de interrogación y espacios​

patron = '[.,? ]+'

#Utilizamos re.split() para dividir el texto según el patrón definido​

partes = re.split(patron, texto)

print("Partes del texto después de dividir:")

for parte in partes:

    print(parte)