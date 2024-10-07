# Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los
# próximos Juegos Panamericanos. Para eso encargó la realización de un programa
# que incluya las siguientes funciones:


# GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas
# disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una
# línea distinta. Ejemplo:
# <Deporte 1>
# <altura del atleta 1>
# <altura del atleta 2>
# < . . . >
# <Deporte 2>
# <altura del atleta 1>
# <altura del atleta 2>
# < . . . >

# GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atle-
# tas, leyendo los datos del archivo generado en el paso anterior. La disciplina y el
# promedio deben grabarse en líneas diferentes. Ejemplo:
# <Deporte 1>
# <Promedio de alturas deporte 1>
# Deporte 2>
# <Promedio de alturas deporte 2>
# < . . . >

# mostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas
# superan la estatura promedio general. Obtener los datos del segundo archivo

def validarNumero():
    while True: 
        try: 
            numero = float(input("Ingrese la altura del atleta "))
            break
        except ValueError: 
            print("por favor ingrese un numero ")

    return numero

def grabarAlturas(): 
    archivoAlturas = 'archivoAlturas.txt'
    try: 
        archivoAbierto = open(archivoAlturas, mode= 'wt')
    except IOError: 
        print("El archivo de alturas no se pudo abrir con exito ")

    disciplina = input("Ingrese la disciplina de los atletas -1 para finalizar ")
    while disciplina != -1: 
        
        disciplina = disciplina.upper()
        archivoAbierto.write("DISCIPLINA: " + disciplina + "\n")
        print("ingrese la altura de los atletas, -1 para finalizar con esta disciplina")
        numero = validarNumero()
        while numero != -1:
            numero = str(numero)
            linea = "Altura: "+ numero+ "\n"
            #str(linea)
            archivoAbierto.write(linea)
            numero = validarNumero()

        disciplina = input("Ingrese la siguiente disciplina ")
    
    try: 
        archivoAbierto.close()
    except IOError: 
        print("El archivo de alturas no se pudo cerrar con exito")

grabarAlturas()