import matplotlib
matplotlib.use('Agg')  # Usa el backend 'Agg' para gráficos sin interfaz gráfica

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Cargar los datos
datos = pd.read_csv('moviescs.csv')
df = pd.DataFrame(datos)

# Selección de columnas para clustering
x = df['cast_total_facebook_likes'].values
y = df['imdb_score'].values

# Cálculo del valor promedio de likes
print('Valor promedio de likes:', df['cast_total_facebook_likes'].mean())

# Matriz de características
info = df[['cast_total_facebook_likes', 'imdb_score']].to_numpy()
print(info)

# Crear una matriz numpy con las coordenadas para clustering
X = np.array(list(zip(x, y)))
print(X)

# Creación del modelo KMeans
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_
colors = ["m.", "r.", "c.", "y.", "b."]

# Visualización de los clusters y centroides
for i in range(len(X)):
    print("Coordenadas:", X[i], "Label:", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)

plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=150, linewidths=5, zorder=10)
plt.xlabel('Total de likes en Facebook del elenco')
plt.ylabel('Puntaje IMDb')
plt.title('Clustering de Películas por Likes y Puntaje IMDb')
plt.savefig("grafica_ejercicio2.png")  # Guarda la gráfica en un archivo
