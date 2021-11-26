import re

def aplicar_regex(cadena):
    # Identificar palabras seguidas de un espacio y una única letra mayúscula
    patron1 = '[0-9A-Za-z]+\s[A-Z][\s.,EOL\n]'

    # Identificar correos válidos
    patron2 = '^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$'

    # Identificar números de tarjeta de crédito separados por - o espacios en blanco, en paquetes de 4 dígitos.
    patron3 = '[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}|[0-9]{4}\s[0-9]{4}\s[0-9]{4}\s[0-9]{4}'


    #print("Mete cosas")
    #cadena = input()

    res = re.match(patron1, cadena)
    if res:
        return("He encontrado tu palabra seguida de mayúscula")

    res = re.match(patron2, cadena)
    if res:
        return("He encontrado tu correo")

    res = re.match(patron3, cadena)
    if res:
        return("He encontrado tu cosa")