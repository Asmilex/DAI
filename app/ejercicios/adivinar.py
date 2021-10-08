# Programe un mini-juego de "adivinar" un número (entre 1 y 100) que el ordenador establezca al azar.
# El usuario puede ir introduciendo números y el ordenador le responderá con mensajes del estilo
# "El número buscado el mayor / menor". El programa debe finalizar cuando el usuario adivine el número
# (con su correspondiente mensaje de felicitación) o bien cuando el usuario haya realizado
# 10 intentos incorrectos de adivinación.


from random import seed
from random import randint

seed(1)

valor = randint(1, 100)

intentos_disponibles = 10

while intentos_disponibles >= 0:
    print("Introduce un número: ")
    num = int(input())

    if num < valor:
        print("Dale dale que te has quedado corto")
    elif num > valor:
        print("Te has pasado fiera")
    else:
        print("Qué máquina eres que lo has clavao")
        break
