import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(10000)
y = np.random.rand(10000)

# Diagrama de dispersión sin transparencia (alta sobreposición)
plt.scatter(x, y)
plt.title("Dispersión con Alta Sobreposición")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.show()

# Diagrama de dispersión con transparencia para mejorar visibilidad
plt.scatter(x, y, alpha=0.1)
plt.title("Dispersión con Transparencia Reducida")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.show()
