#Este programa hace la division mostrando el resto

print("Escribe el dividendo:")
dividendo = float(input())

print("Escribe el divisor:")
divisor = float(input())

#operaciones
division = dividendo // divisor
resto = dividendo % divisor

#imprimimos por pantalla
print(f"El cociente es: {division}")
print(f"El resto es: {resto}")
