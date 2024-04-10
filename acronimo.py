nombre = input("Porfavor ingrese el significado de una organizacion: ")
acronimo = nombre.split()
nc = ""

for i in acronimo:
    nc += i[0]

print(nc)