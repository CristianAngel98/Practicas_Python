with open("texto.txt", 'w' ) as texto:
    texto.write("Bien, hoy es el día en el que me voy a crear un desarrollador experto")

#with open("texto.txt", 'a' ) as texto:
#   texto.write("Esta es la segunda parte del texto con append \n")

with open("texto.txt", 'r' ) as texto:
    #contador = 0
    o = texto.readline().split()
    print (len(o))
