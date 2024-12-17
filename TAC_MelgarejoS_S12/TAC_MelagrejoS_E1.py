from sklearn.datasets import fetch_openml
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score

# Cargar el conjunto de datos de diabetes desde OpenML
diabetes = fetch_openml(name='diabetes', version=1)

# Verificar el tipo de datos de y
print(diabetes.target[:10])  # Imprime los primeros 10 valores de la variable objetivo

# Si y tiene valores categóricos, los transformamos
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(diabetes.target)

# Dividir los datos en entrenamiento y prueba
X = diabetes.data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error (MSE): {mse}')
print(f'R^2: {r2}')
input(' ')