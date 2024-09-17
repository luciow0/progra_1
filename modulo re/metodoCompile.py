# La compilación de expresiones regulares es el  proceso mediante el cual una expresión  regular 
# se convierte en un objeto patrón que  puede ser reutilizado eficientemente.​
# La ventaja de compilar una expresión regular  es que permite optimizar las búsquedas, 
# especialmente cuando la misma expresión se  utiliza múltiples veces en el código.​
# Al compilar una expresión regular, no solo se  mejora la legibilidad del código, sino también  su rendimiento, 
# ya que evita la necesidad de  recompilar la misma expresión en cada uso.​

import re

patron = re.compile('[0-9]{4}')

cadena = "07/08/2017|03/02/1984|17/03/1984"

coincidencias = patron.findall(cadena)

print(f'Coincidencias encontradas con findall(): {coincidencias}')

inicioCoincidencia = patron.match(cadena)  

print(f'Coincidencia al inicio con match(): {inicioCoincidencia}')

cadenaReemplazada = patron.sub('XXXX', cadena)  

print(f'Cadena después de usar sub(): {cadenaReemplazada}')