print("intoduce el primer valor:")
valor1 = float(input())

print("intoduce el segundo valor:")
valor2 = float(input())

print("introduce la suma de los numeros:")
suma = float(input())

suma_pc = valor1 + valor2
diferencia = valor1/valor2*100

if suma == suma_pc:
    print("has hecho bien la suma")
else:
    print(f"No esta bien la suma, {valor1} + {valor2} = {suma_pc}")
    print(f"la diferencia es del {diferencia}")
