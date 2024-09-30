def ingresarNumerosNaturales():   
    try: 
        num = int(input("Ingrese un numero "))

        if type(num) == str: 
            raise OverflowError

        if type(num) == float: 
            raise IndexError

        assert num > 0

    except IndexError: 
        print("tenias que ingrear un num no un float")

    except AssertionError: 
        print("debias ingresar un numero mayor a 0")

    except OverflowError: 
        print("tenias que ingresar un entero no un str")



    else: 
        print("aca esta tu num perro ",num)


ingresarNumerosNaturales()