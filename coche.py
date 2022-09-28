#calcular precio de un coche
precioCoche = float(input("Introduzca el precio del coche: "))
kilometros = float(input("Introduzca los kilometros que vas a hacer: "))
gasolina = float(input("Introduzca el precio de la gasolina: "))
consumo = float(input("Introduzca los kilometros por litro de gasolina que hace el coche: "))

precioTotal = (kilometros / consumo) * gasolina + precioCoche

print(f"El precio total del coche es: {precioTotal}")
