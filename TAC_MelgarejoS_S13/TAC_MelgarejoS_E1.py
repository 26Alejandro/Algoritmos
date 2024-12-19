import matplotlib
from wx.lib.pubsub.py2and3 import values

matplotlib.use('Agg')  # Usa el backend 'Agg' para gráficos sin interfaz gráfica

from pydataset import data
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

# Carga del dataset
pima = data('Pima.tr')

# Gráfico de dispersión
pima.plot(kind='scatter', x='skin', y='bmi', color='blue', alpha=0.5)
plt.xlabel('Grosor de la piel (skin)')
plt.ylabel('Índice de masa corporal (bmi)')
plt.savefig('scatter_plot.png')  # Guarda la imagen en un archivo
plt.clf()  # Limpia el gráfico para evitar superposición en la siguiente gráfica

# División de datos en entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(pima.skin, pima.bmi, test_size=0.3)

# Gráfico de datos de entrenamiento y prueba
plt.scatter(x_train, y_train, label='Entrenamiento de datos', color='red', alpha=0.7)
plt.scatter(x_test, y_test, label='Prueba de datos', color='green', alpha=0.7)
plt.xlabel('Grosor de la piel (skin)')
plt.ylabel('Índice de masa corporal (bmi)')
plt.legend()
plt.title('Entrenamiento y prueba de datos (Train-Test Split)')
plt.savefig('train_test_split.png')
plt.clf()  # Limpia el gráfico

# Creación del modelo de regresión lineal
LR = LinearRegression()
LR.fit(x_train.values.reshape(-1, 1), y_train.values)

# Predicción usando el conjunto de prueba
prediccion = LR.predict(x_test.values.reshape(-1, 1))

# Gráfico de la regresión lineal
plt.scatter(x_test, y_test, label='Datos de prueba', color='green', alpha=0.7)
plt.plot(x_test, prediccion, label='Regresión lineal', color='blue')
plt.xlabel('Grosor de la piel (skin)')
plt.ylabel('Índice de masa corporal (bmi)')
plt.legend()
plt.title('Modelo de regresión lineal')
plt.savefig('linear_regression.png')
#ahora pondremos a prueba nuestro sistema de reregresion lineal
#para un BMI para la medida cutanea 50
valor_aprox=LR.predict(np.array([[50]]))[0]
print(valor_aprox)

valor_test= LR.score(x_test.values.reshape(-1,1), y_test.values)
print(valor_test)
