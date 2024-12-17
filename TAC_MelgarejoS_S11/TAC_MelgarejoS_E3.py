import pandas as pd

# Pedir al usuario que ingrese el número de empleados
num_empleados = int(input("Ingrese el número de empleados: "))

# Crear listas para almacenar los datos de los empleados
nombres = []
edades = []
salarios = []

# Solicitar información de cada empleado
for i in range(num_empleados):
    nombre = input(f"Ingrese el nombre del empleado {i + 1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    salario = float(input(f"Ingrese el salario de {nombre}: "))

    nombres.append(nombre)
    edades.append(edad)
    salarios.append(salario)

# Crear un DataFrame a partir de los datos ingresados
data = {
    "Nombre": nombres,
    "Edad": edades,
    "Salario": salarios
}
df = pd.DataFrame(data)
print("\nDataFrame de empleados:")
print(df)

# Calcular estadísticas básicas
print("\nEstadísticas básicas:")
print(df.describe())  # Estadísticas como media, desvío estándar, valores mínimos y máximos

# Filtrar empleados con salario mayor a un umbral ingresado por el usuario
umbral_salario = float(input("\nIngrese el umbral de salario para filtrar empleados: "))
empleados_altos_salarios = df[df["Salario"] > umbral_salario]
print(f"\nEmpleados con salario mayor a {umbral_salario}:")
print(empleados_altos_salarios)

# Agregar una nueva columna 'Salario Anual'
df["Salario Anual"] = df["Salario"] * 12
print("\nDataFrame con la columna 'Salario Anual':")
print(df)

# Agrupar por edad y calcular el salario promedio por grupo de edad
salario_promedio_por_edad = df.groupby("Edad")["Salario"].mean()
print("\nSalario promedio por edad:")
print(salario_promedio_por_edad)
