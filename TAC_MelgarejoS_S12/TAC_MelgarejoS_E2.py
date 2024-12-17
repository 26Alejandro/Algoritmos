from sklearn.datasets import make_blobs
import numpy as np
from dearpygui import dearpygui as dpg

# Generar datos de muestra con blobs
blob_centers = np.array(
    [[0.2, 2.3],
     [-1.5, 2.3],
     [-2.8, 1.8],
     [-2.8, 2.8],
     [-2.8, 1.3]]
)
blob_std = np.array([0.4, 0.3, 0.1, 0.1, 0.1])

X, y = make_blobs(n_samples=2000, centers=blob_centers,
                  cluster_std=blob_std, random_state=7)

# Crear puntos para graficar
x = X[:, 0]
y = X[:, 1]

# Configurar Dear PyGui
dpg.create_context()
dpg.create_viewport(title='Dear PyGui Scatter Plot', width=600, height=400)

with dpg.window(label="Scatter Plot"):
    with dpg.plot(label="Sample Plot"):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="X axis")
        y_axis = dpg.add_plot_axis(dpg.mvYAxis, label="Y axis")
        dpg.add_scatter_series(x, y, label="Cluster Points", parent=y_axis)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
