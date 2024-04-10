from random import randint

choice = ["roca", "papel", "tijeras"]
computerChoice = choice[randint(0, 2)]

print("***Bienvenido al juego de piedra, papel o tijera\n")
userChoice = input("Escoge por favor: ").lower()

print("Eleccion de la maquina: " + computerChoice)

if userChoice == computerChoice:
    print("EMPATE *-*")

elif userChoice == "roca" and computerChoice == "tijeras":
    print("¡¡¡HAZ GANADO!!!")

elif userChoice == "tijeras" and computerChoice == "roca":
    print("¡¡¡HAZ PERDIDO!!!")

elif userChoice == "roca" and computerChoice == "papel":
    print("HAZ PERDIDO *n*")

elif userChoice == "papel" and computerChoice == "roca":
    print("HAZ GANADO :)")

elif userChoice == "tijeras" and computerChoice == "papel":
    print("HAZ GANADO")

elif userChoice == "papel" and computerChoice == "tijeras":
    print("HAZ PERDIDO")

