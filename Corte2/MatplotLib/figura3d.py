import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Gráfica 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.title("Gráfica 3D de Superficie")
plt.show()

# Gráfico de contorno 2D
plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar(label='Valor de Z')
plt.title("Mapa de Contorno 2D")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
