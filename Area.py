print("Escribe el radio de la circunferencia")
radio = input()

PI = 3.416

perimetro = 2 * PI * int(radio)
area = PI * (int(radio) ** 2)

print("El perimetro es: %d" %perimetro)
print("El area es %d" %area)
