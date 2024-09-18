def devolverCadena(cadena, n):
    inicio = len(cadena) - n 
    subCadena = ''
    for i in range(inicio, len(cadena)): 
        subCadena += cadena[i]
    
    return subCadena

cadenaPrueba = "mcs desconformes, para ser feliz faltan años"
n = int(input("Ingrese la cantitdad de caracteres que desea crear la nueva cadena que empieza desde el final no se es medio raro de explicar "))
check = devolverCadena(cadenaPrueba, n)
print(check)