factura = float(input("Por favor ingrese el total de la factura de hoy: "))

def tipoPropina(factura):
    tipoPropina = 0
    while tipoPropina not in [1, 2, 3]:
        print("ingrese 1 Si desea dejar 18 % de propina\n ------------")
        print("ingrese 2 Si desea dejar 20 % de propina\n ------------")
        print("ingrese 3 Si desea dejar 25 % de propina\n ------------")
        
        tipoPropina = int(input("Ingrese por favor el numero para determinar la propina:  "))
        if tipoPropina == 1:    
            propina = round(factura * 0.18, 2)
            total = factura + propina
            return propina, total

        elif tipoPropina == 2:    
            propina = round(factura  * 0.20, 2)
            total = factura + propina
            return propina, total

        elif tipoPropina == 3:    
            propina = round(factura  * 0.25, 2)
            total = factura + propina
            return propina, total
        
       
# pip install --user nombre_del_paquete


propina, total = tipoPropina(factura)
print(f"La propina es: {propina}")
print(f"El total con la propina es: {total}")

personas = int(input("Porfavor ingrese el numero de personas para dividir la cuenta: "))

print("El total que debe pagar cada persona es:  " + str(total / personas))

