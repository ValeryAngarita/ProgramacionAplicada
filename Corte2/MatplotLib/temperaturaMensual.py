import matplotlib.pyplot as plt
import numpy as np

dias = np.arange(1, 32)
temperatura = np.random.randint(12, 28, size=31)

plt.plot(dias, temperatura)
plt.title("Temperatura Diaria en Marzo")
plt.xlabel("Día")
plt.ylabel("Temperatura (°C)")

plt.savefig("temperatura_diaria_marzo.png", dpi=300, bbox_inches='tight')
plt.savefig("temperatura_diaria_marzo.pdf", format='pdf', bbox_inches='tight')
