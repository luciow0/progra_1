def verificarFecha(dia,mes,año): 
    valido = False
    dias = [31,28,31,30,31,30,31,31,30,31,30,31]

    if dia >= dias[mes]: 
        valido = True
        
    return valido
