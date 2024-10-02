def guardarApellidos(): 
    try: 
        arch = open("/home/luciowo/progra_1/ejericios_guia/tp6/ej1/nombres y apellidos.txt", mode = 'rt')

    except IOError: 
        print("El archivo nombres y apellidos no se pudo abrir correctamente ")

    linea = arch.readline()

    while linea: 
        apellido, nombre = linea.split(",")
        apellido = apellido.upper()
        armenio = True
        while armenio: 
            if apellido[-1] != "N": 
                armenio = False
            if apellido[-2] != "A": 
                armenio = False
            if apellido[-3] != "O": 
                armenio = False

        if armenio: 
            try: 
                archivoArmenia = open("/home/luciowo/progra_1/ejericios_guia/tp6/ej1/ARMENIA.txt", mode = 'wt')
            except IOError: 
                print("No se pudo abrir el archivoArmenia con exito ")
            
            else: 
                archivoArmenia.write(linea + "\n")
                try: 
                    archivoArmenia.close()
                except IOError: 
                    print("El arhcivoArmenia no se pudo cerrar ")

    #########################################################################################

        italiano = True
        while italiano: 
            if apellido[-1] != "I": 
                italiano = False
            if apellido[-2] != "A": 
                italiano = False
            if apellido[-3] != "N": 
                italiano = False

        if italiano: 
            try: 
                archivoItalia = open("/home/luciowo/progra_1/ejericios_guia/tp6/ej1/ITALIA.txt", mode = 'wt')
            except IOError: 
                print("No se pudo abrir el archivoItalia con exito ")
            
            else: 
                archivoItalia.write(linea + "\n")
                try: 
                    archivoItalia.close()
                except IOError: 
                    print("El archivoItalia no se pudo cerrar correctamente")

    #######################################################################################

        español = True
        while español: 
            if apellido[-1] != "N": 
                español = False
            if apellido[-2] != "A": 
                español = False
            if apellido[-3] != "O": 
                español = False

        if español: 
            try: 
                archivoEspaña = open("/home/luciowo/progra_1/ejericios_guia/tp6/ej1/ESPAÑA.txt", mode = 'wt')
            except IOError: 
                print("No se pudo abrirEspaña el archivo con exito ")
            
            else: 
                archivoEspaña.write(linea + "\n")
                try: 
                    archivoEspaña.close()

                except IOError: 
                    print("El archivoEspaña no se pudo cerrar correctamente")

        linea = arch.readline()

    else: 
        try: 
            arch.close()
        except IOError: 
            print("El archivo nombres y apellidos no se pudo cerrar correctamente ")



def mostrarApellidos(): 
    try: 
        archivoArmenia = open("/home/luciowo/progra_1/ejericios_guia/tp6/ej1/ARMENIA.txt", mode = 'rt')
    except IOError: 
        print("No se pudo abrir el archivoArmenia con exito nooo aca")

    else: 
        #linea = archivoArmenia.readline()
        #while linea: 
        #    print(linea)
        #    linea = archivoArmenia.readline()
        for linea in archivoArmenia: 
            print(linea.strip())

        try: 
            archivoArmenia.close()

        except IOError: 
            print("No se pudo cerrar correctamente el archivoArmenia ")

###############################################################################################    

    try: 
        archivoItalia = open("/home/luciowo/progra_1/ejericios_guia/tp6/ej1/ITALIA.txt", mode = 'rt')
    except IOError: 
        print("No se pudo abrir el archivoItalia con exito ")

    else: 
        linea = archivoItalia.readline()
        while linea: 
            print(linea)
            linea = archivoItalia.readline()

        try: 
            archivoItalia.close()

        except IOError: 
            print("No se pudo cerrar correctamente el archivoItalia ")
        
###############################################################################################    

    try: 
        archivoEspaña = open("/home/luciowo/progra_1/ejericios_guia/tp6/ej1/ESPAÑA.txt", mode = 'rt')
    except IOError: 
        print("No se pudo abrir el archivoEspaña con exito ")

    else: 
        linea = archivoEspaña.readline()
        while linea: 
            print(linea.strip())
            linea = archivoEspaña.readline()

        try: 
            archivoEspaña.close()

        except IOError: 
            print("No se pudo cerrar correctamente el archivoEspaña ")
    
guardarApellidos() 
mostrarApellidos()