"""
charfun.py
Programa que determina si una cadena proporcionada por el
usuario es palíndroma. Para ello se preguntará por teclado al
usuario tantas veces como quiera hasta que escriba la palabra
salir.
Ultima Modificación. 21/11/2024
Autor. Gregorio Coronado Morón
Dependencias. Unicodedata
"""
import re

"""
    Función que verifica si una cadena es palíndroma.
    Ignora espacios, mayúsculas y tildes.
    version base
"""

# def esPalindromo(cadena):

#     # Convertir la cadena a minúsculas y eliminar caracteres no alfabéticos
#     cadena_limpia = ''.join(char.lower() for char in cadena if char.isalnum())
#     # Comparar la cadena limpia con su reverso
#     return cadena_limpia == cadena_limpia[::-1]



# Version mejorada

def esPalindromo(cadena):

    # Convertir la cadena a minúsculas para ignorar diferencias de mayúsculas y minúsculas
    cadena = cadena.lower()
    
    # Eliminar todos los caracteres no alfanuméricos (espacios, puntuación, tildes)
    cadena = re.sub(r'[^a-z0-9]', '', cadena)
    
    # Verificar si la cadena es igual a su reverso
    return cadena == cadena[::-1]

