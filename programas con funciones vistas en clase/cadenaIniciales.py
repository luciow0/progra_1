cadena = "universidad argentina de la empresa"
cant = cadena.count(" ")
for i in range(cant):
    aux = cadena.index(" ")
    rebanda = cadena[0:aux]
    print(rebanda)
    rebanda = rebanda.upper()
    print(rebanda)
    inicial += rebanda[0]
    print(inicial)
    