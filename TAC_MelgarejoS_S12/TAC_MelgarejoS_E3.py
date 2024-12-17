from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter

# Crear datos de ejemplo
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=2000, centers=4, cluster_std=1.0, random_state=11)

# Lista para almacenar modelos de KMeans y puntajes de silueta
kmeans_per_k = []
silhouette_scores = []

# Entrenar modelos KMeans para valores de k de 3 a 8
for k in range(3, 9):  # Ajustar rango para 3 a 8
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    kmeans_per_k.append(kmeans)

    # Calcular el promedio del coeficiente de silueta para cada k
    silhouette_avg = silhouette_score(X, kmeans.labels_)
    silhouette_scores.append(silhouette_avg)

# Gráfico de coeficientes de silueta
plt.figure(figsize=(14, 12))  # Ajustar tamaño de la figura para acomodar más subgráficos

for k in (3, 4, 5, 6, 7, 8):  # Considerar todos los valores de k
    plt.subplot(2, 3, k - 2)  # Cambiar a 2 filas y 3 columnas

    y_pred = kmeans_per_k[k - 3].labels_
    silhouette_coefficients = silhouette_samples(X, y_pred)

    padding = len(X) // 30
    pos = padding
    ticks = []
    for i in range(k):
        coeffs = silhouette_coefficients[y_pred == i]
        coeffs.sort()

        color = matplotlib.cm.Spectral(i / k)
        plt.fill_betweenx(np.arange(pos, pos + len(coeffs)), 0, coeffs,
                          facecolor=color, edgecolor=color, alpha=0.7)
        ticks.append(pos + len(coeffs) // 2)
        pos += len(coeffs) + padding

    plt.gca().yaxis.set_major_locator(FixedLocator(ticks))
    plt.gca().yaxis.set_major_formatter(FixedFormatter(range(k)))
    if k in (3, 5):
        plt.ylabel("Cluster")

    if k in (5, 6):
        plt.gca().set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])
        plt.xlabel("Silhouette Coefficient")
    else:
        plt.tick_params(labelbottom=False)

    # Trazar línea vertical para el promedio del coeficiente de silueta
    plt.axvline(x=silhouette_scores[k - 3], color="red", linestyle="--")
    plt.title("$k={}$".format(k), fontsize=16)

plt.tight_layout()
plt.savefig('melgarejo1.png')  # Guarda la imagen como melgarejo
