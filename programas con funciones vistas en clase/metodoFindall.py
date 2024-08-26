import re

texto = "Juan tiene el télefono 1234-5678, Oliver tiene el  teléfono 11-15-3456-7890 y Gabriela el 11-15-7654-3210."

patron = "([0-9]{2})-(15-[0-9]{4})-([0-9]{4})"

numeros = re.findall(patron, texto)



#Imprimimos los números de celulares encontrados y sus partes  específicas​

if numeros:

    print("Números de celulares encontrados:") 

    for numero in numeros:

        print(f"Número completo: {numero[0]}-{numero[1]}-{numero[2]}")
   
        print(f"Código de área: {numero[0]}")  

        print("----")

else:

    print("No se encontraron números de teléfono.")