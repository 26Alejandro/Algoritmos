import numpy as np

# Pedir al usuario el tamaño de la matriz
n = int(input("Ingrese el tamaño de la matriz cuadrada (ejemplo: 3 para una matriz 3x3): "))

# Crear una matriz aleatoria de tamaño nxn con valores entre 0 y 10
matriz = np.random.randint(0, 10, (n, n))
print("\nMatriz generada aleatoriamente:")
print(matriz)

# Calcular la transpuesta de la matriz
transpuesta = np.transpose(matriz)
print("\nTranspuesta de la matriz:")
print(transpuesta)

# Calcular el determinante de la matriz
determinante = np.linalg.det(matriz)
print(f"\nDeterminante de la matriz: {determinante}")

# Calcular la inversa de la matriz (si el determinante no es cero)
if determinante != 0:
    inversa = np.linalg.inv(matriz)
    print("\nInversa de la matriz:")
    print(inversa)
else:
    print("\nLa matriz no tiene inversa (determinante es 0).")

# Calcular la suma de todos los elementos de la matriz
suma_total = np.sum(matriz)
print(f"\nSuma de todos los elementos de la matriz: {suma_total}")

# Calcular la media de los elementos de la matriz
media = np.mean(matriz)
print(f"Media de los elementos de la matriz: {media}")
