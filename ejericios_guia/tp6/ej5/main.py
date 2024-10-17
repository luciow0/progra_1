# Se dispone de dos formatos diferentes de archivos de texto en los que se almace-
# nan datos de empleados, detallados más abajo. Desarrollar un programa para con-
# vertir cada uno de los formatos suministrados, grabando los datos obtenidos en
# otro archivo con formato CSV. Los archivos de entrada pueden generarse con Block
# de Notas o cualquier otro editor, copiando y pegando los ejemplos proporcionados.
# Ambos archivos tienen tres campos por registro: Apellido y Nombre, Fecha de alta
# y Domicilio.
# Formato 1: Los campos tienen longitud fija con un espacio de separación
# entre ellos.
# (Regla) 1 2 3 4 5 6                                                ♥
# 012345678901234567890123456789012345678901234567890123456789012
# Pérez Juan 20080211 Corrientes 348
# González Ana M 20080115 Juan de Garay 1111 3er piso dto A
# Formato 2: Todos los campos de este archivo están precedidos por un
# número de dos dígitos que indica la longitud del campo que sigue.
# 10Pérez Juan082008021114Corrientes 348
# 14González Ana M082008011533Juan de Garay 1111 3er piso dto A
# NOTAS:
# ∑ Los espacios que se encuentren al final de las cadenas en el formato 1 deberán
# ser eliminados.
# ∑ El formato 2 debe generalizarse para que soporte registros con cualquier canti-
# dad de campos.