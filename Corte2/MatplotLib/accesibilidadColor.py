import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y_seno = np.sin(x)
y_coseno = np.cos(x)

# Paleta no apta para daltónicos
plt.plot(x, y_seno, color='red', label='seno(x)')
plt.plot(x, y_coseno, color='green', label='coseno(x)')
plt.title("Gráfica con Colores Poco Accesibles")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

# Paleta apta para daltónicos
plt.plot(x, y_seno, color='#0072B2', label='seno(x)')   # Azul
plt.plot(x, y_coseno, color='#D55E00', label='coseno(x)')  # Naranja
plt.title("Gráfica con Colores Accesibles")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
