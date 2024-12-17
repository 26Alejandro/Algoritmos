import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons

# Crear datos sintéticos (dos medios círculos)
X, _ = make_moons(n_samples=300, noise=0.1, random_state=0)

# Aplicar DBSCAN con parámetros epsilon=0.2 y min_samples=5
dbscan = DBSCAN(eps=0.2, min_samples=5)
dbscan.fit(X)

# Obtener las etiquetas de los clusters
labels = dbscan.labels_

# Visualización de los datos y los clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.title('DBSCAN Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
