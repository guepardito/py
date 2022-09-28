#Este programa calcula la hipotenusa segun el teorema de pitagoras

print("intoduce el valor del primer cateto:")
cateto1 = float(input())

print("intoduce el valor del segundo cateto:")
cateto2 = float(input())

#Teorema segun los catetos
hipotenusa = float((cateto1 ** 2 + cateto2 ** 2) ** (1/2))

print("El lado de la hipotenusa es: %.1f " %hipotenusa)
