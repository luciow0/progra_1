import re

cadenas = ['A123', 'B456', 'C789', '123A', 'D1234']
patron = '[A-Za-Z][0-9]{3}'

for cadena in cadenas: 
    if re.match(patron,cadena): 
        print('a pleno perrito')
    else: 
        print('te quisiste hacer el zarpado y no te salio ')