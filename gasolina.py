#calcular el consumo de gasolina de un coche :)
litros = float(input("Escribe cuántos litros de gasolina has usado: "))
kilometros = float(input("escribe cuantos kilometros has recorrido: "))
consumo = (100/kilometros)*litros

print(f"el coche consume {consumo} l/100km")
