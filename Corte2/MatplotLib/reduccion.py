import matplotlib.pyplot as plt
import numpy as np

x_grande = np.linspace(0, 100, 10000)
y_grande = np.sin(x_grande) + np.random.normal(0, 0.1, size=x_grande.shape)

x_reducido = x_grande[::10]
y_reducido = y_grande[::10]

plt.plot(x_reducido, y_reducido)
plt.title("Gráfica con Datos Reducidos")
plt.xlabel("Eje X")
plt.ylabel("Valor Medido")
plt.show()
