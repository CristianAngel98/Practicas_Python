"""
from random import randint
numUser = int(input("Porfavor ingrese un numero del 0 al 50: "))
numAleatorio = randint(1,50)
contador = 0

while numAleatorio != numUser:
    if numUser == numAleatorio:
        print("HAZ GANADO y te tomo " + {contador} + " intentos")
    else:
        print("HAZ PERDIDO, Intentalo de nuevo" + str(numAleatorio))
        numUser = int(input("Porfavor ingrese un numero del 0 al 50: "))
        contador += 1
"""

from random import randint

numUser = int(input("Por favor ingrese un número del 0 al 50: "))
numAleatorio = randint(1, 50)
contador = 0

while numUser != numAleatorio:
    print("Has perdido, inténtalo de nuevo.")
    if numUser < numAleatorio:
        print("El número es mayor.")
    else:
        print("El número es menor.")
    numUser = int(input("Por favor ingrese un número del 0 al 50: "))
    contador += 1

print("¡Has ganado en", contador, "intentos!")
