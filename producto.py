
# Programa para calcular el producto punto de dos vectores

n = int(input("Ingrese la dimensión de los vectores: "))

vector1 = []
vector2 = []

print("\nIngrese los datos del Vector 1")
for i in range(n):
    valor = float(input(f"Componente {i + 1}: "))
    vector1.append(valor)

print("\nIngrese los datos del Vector 2")
for i in range(n):
    valor = float(input(f"Componente {i + 1}: "))
    vector2.append(valor)

producto = 0
for i in range(n):
    producto += vector1[i] * vector2[i]

print("\nVector 1:", vector1)
print("Vector 2:", vector2)
print("Producto punto:", producto)
