import matplotlib
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

