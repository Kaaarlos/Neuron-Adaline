import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
puntitosx = []
puntitosy = []
def adaline_filter(X, y, learning_rate=0.01, n_epochs=100):
    # Normalizamos las características de entrada
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Inicializamos los pesos aleatoriamente
    weights = np.random.rand(X_scaled.shape[1])
    bias = np.random.rand()
    
    # Entrenamos el modelo durante el número de épocas especificado
    for epoch in range(n_epochs):
        # Calculamos la salida del modelo para cada muestra
        output = np.dot(X_scaled, weights) + bias
        
        # Calculamos el error y actualizamos los pesos y el sesgo
        error = y - output
        weights += learning_rate * np.dot(X_scaled.T, error)
        bias += learning_rate * np.sum(error)
    
    # Devolvemos los pesos y el sesgo entrenados
    puntitosx.append(weights)
    puntitosy.append(bias)
    return weights, bias

# Ejemplo de uso
# Definimos el array y donde usaremos las primeras 3 posiciones como entrada
x = np.linspace(0, 20, 99)#[::1] # Valores de x de 0 a 100
y = 5*np.sin(x*(2*np.pi/5)) # Función senoidal con amplitud 5

# Escalamos la función para que vaya de 5 a -5 en y
y = -y/2

y += 0.5*(5 - np.min(y)) 

for i in range(len(y)):
    rand_nums = np.random.uniform(-1,1,size=y.shape)
    ee = y + rand_nums

# Creamos un array para almacenar los resultados
results = ee[:3].tolist()

# Generamos las características de entrada y las señales de salida correspondientes
X = np.zeros((len(ee) - 3, 3))
for i in range(len(ee) - 3):
    X[i,:] = ee[i:i+3]

y_out = ee[3:]

# Entrenamos el filtro adaptativo
weights, bias = adaline_filter(X, y_out, learning_rate=0.01, n_epochs=100)

# Predecimos la siguiente posición de la señal 97 veces y la añadimos al array de resultados
X_test = np.zeros((97, 3))
X_test[0,:] = ee[-3:]

for i in range(1, 97):
    X_test[i,:] = np.array([results[-3:]])
    predicted_value = np.dot(X_test[i:i+1,:], weights) + bias
    results.append(predicted_value[0])


print("Resultados:", results)
fig, ax = plt.subplots()
ax.plot(puntitosx, puntitosy, 'o-')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_title("Plano Cartesiano")
ax.plot(x, results, 'o-')
ax.plot(x, ee, 'o-')
plt.show()
