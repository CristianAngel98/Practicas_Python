"""
Par o impar
Lo primero que vamos a realizar es dar la bienvenida preguntando un número entre 1 y 1000

Cuando el usuario proporciona el número, comprobaremos si es par o impar y después imprimimos el mensaje con el resultado.

Ejemplo:

Mensaje que se muestra: ¿En qué número estás pensando?
Entrada: 25
Salida: ¡Es un número impar! ¿Puedes añadir otro?

"""
###SOLUCION

numUser = 1

while numUser > 0:
    numUser = int(input("Por favor ingrese un numero entre 1 y 1000: "))
    if numUser % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es inpar")
    print("************Si desea terminar el juego pulse 0**********")