"""
nombre = input("Por favor ingrese su nombre : ")
while nombre == "*":
    nombre = input("* NO es valido; Por favor ingrese su nombre : ")


fechaNacimiento = input("Por favor ingrese su fecha de nacimiento : ")
while fechaNacimiento == "*":
    fechaNacimiento = input("Por favor ingrese su fecha de nacimiento : ")


direccion = input("Por favor ingrese su direccion : ")
while direccion == "*":
    direccion = input("Por favor ingrese su direccion : ")





print ("NOMBRE: " + nombre + 
       "\nFECHA NACIMIENTO: " + fechaNacimiento +
       "\nDIRECCION: " + direccion)
"""



###OPTIMIZADO CON FUNCION

entrada = ""

def solicitarDatos(mensaje):
    entrada = input(mensaje)
    while entrada == "*":
       entrada =  print("* NO ES VALIDO; ingrese nuevamente un valor correcto: ")
    

nombre = solicitarDatos(input("Ingrese su nombre: "))
diaNacimiento = solicitarDatos(input("Ingrese su dia de nacimiento: "))
direccion = solicitarDatos(input("Ingrese su direccion: "))   
    
print ("NOMBRE: " + nombre + 
    "\nFECHA NACIMIENTO: " + diaNacimiento +
    "\nDIRECCION: " + direccion)

solicitarDatos(entrada)
