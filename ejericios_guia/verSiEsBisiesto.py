def verSiEsBisiesto(año): 
    flag = False
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0): 
        flag =  True
    return flag

