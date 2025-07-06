import matplotlib.pyplot as plt
import numpy as np

edad = np.random.randint(15, 71, size=3000) #Límite superior exclusivo

plt.hist(edad, bins=10, color='c', edgecolor='k')
plt.title("Distribución de edad de participantes")
plt.xlabel("Edad")
plt.ylabel("Número de participantes")
plt.grid(False)
plt.show()
