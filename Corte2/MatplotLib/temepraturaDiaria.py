import matplotlib.pyplot as plt
import numpy as np

dias = np.arange(1, 31)
temperatura = np.random.randint(10, 30, size=30)

plt.plot(dias, temperatura, color='orange', marker='x', linestyle='-')
plt.title("Temperatura Diaria en Abril", fontsize=16)
plt.xlabel("Día", fontsize=12)
plt.ylabel("Temperatura (°C)", fontsize=12)
plt.grid(True)
plt.legend(['Temperatura'], loc='upper right')

dia_max = dias[np.argmax(temperatura)]
temp_max = np.max(temperatura)

plt.annotate('Día más caluroso', xy=(dia_max, temp_max), xytext=(dia_max + 1, temp_max - 4),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.tight_layout()
plt.show()
