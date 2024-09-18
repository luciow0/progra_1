numerosEnLetras = [
    'cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez',
    'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve',
    'veinte', 'veintiuno', 'veintidós', 'veintitrés', 'veinticuatro', 'veinticinco', 'veintiséis',
    'veintisiete', 'veintiocho', 'veintinueve', 'treinta', 'treinta y uno', 'treinta y dos', 'treinta y tres',
    'treinta y cuatro', 'treinta y cinco', 'treinta y seis', 'treinta y siete', 'treinta y ocho', 'treinta y nueve',
    'cuarenta', 'cuarenta y uno', 'cuarenta y dos', 'cuarenta y tres', 'cuarenta y cuatro', 'cuarenta y cinco',
    'cuarenta y seis', 'cuarenta y siete', 'cuarenta y ocho', 'cuarenta y nueve', 'cincuenta', 'cincuenta y uno',
    'cincuenta y dos', 'cincuenta y tres', 'cincuenta y cuatro', 'cincuenta y cinco', 'cincuenta y seis',
    'cincuenta y siete', 'cincuenta y ocho', 'cincuenta y nueve', 'sesenta', 'sesenta y uno', 'sesenta y dos',
    'sesenta y tres', 'sesenta y cuatro', 'sesenta y cinco', 'sesenta y seis', 'sesenta y siete', 'sesenta y ocho',
    'sesenta y nueve', 'setenta', 'setenta y uno', 'setenta y dos', 'setenta y tres', 'setenta y cuatro',
    'setenta y cinco', 'setenta y seis', 'setenta y siete', 'setenta y ocho', 'setenta y nueve', 'ochenta',
    'ochenta y uno', 'ochenta y dos', 'ochenta y tres', 'ochenta y cuatro', 'ochenta y cinco', 'ochenta y seis',
    'ochenta y siete', 'ochenta y ocho', 'ochenta y nueve', 'noventa', 'noventa y uno', 'noventa y dos',
    'noventa y tres', 'noventa y cuatro', 'noventa y cinco', 'noventa y seis', 'noventa y siete', 'noventa y ocho',
    'noventa y nueve'
]

#100,000,000,0000 1 billon

#

def convertirNumero(entero, numerosEnLetras):
    nuemeroString = '' 
    if entero >= 1000000000000: 
        inicio = str(entero)
        inicio = inicio[0]
        inicio = int(inicio)
        string = numerosEnLetras[inicio]
        nuemeroString += (string + ' ' + 'billon/es') #manejar caso del uno
        print(nuemeroString)

    elif entero > 1000000: 
        inicio = str(entero)
        inicio = inicio[0]
        inicio = int(inicio)
        string = numerosEnLetras[inicio]
        nuemeroString += (string + ' ' + 'millon/es') #manejar caso del uno
        print(nuemeroString)

check = convertirNumero(5000000000000, numerosEnLetras)