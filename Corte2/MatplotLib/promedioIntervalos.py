import matplotlib.pyplot as plt
import numpy as np

x_grande = np.linspace(0, 100, 10000)
y_grande = np.sin(x_grande) + np.random.normal(0, 0.1, size=x_grande.shape)

intervalos = np.linspace(0, 100, 100)
y_promediado = [np.mean(y_grande[(x_grande >= intervalos[i]) & (x_grande < intervalos[i+1])]) for i in range(len(intervalos)-1)]

plt.plot(intervalos[:-1], y_promediado)
plt.title("Gráfica de Datos Promediados por Intervalo")
plt.xlabel("Eje X")
plt.ylabel("Promedio")
plt.show()
