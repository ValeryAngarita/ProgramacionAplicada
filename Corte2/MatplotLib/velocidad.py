import matplotlib.pyplot as plt
import numpy as np

velocidades = np.random.normal(loc=25, scale=5, size=1000)
plt.violinplot(velocidades)
plt.title("Distribución de Velocidades Promedio")
plt.ylabel("Velocidad (km/h)")
plt.show()
