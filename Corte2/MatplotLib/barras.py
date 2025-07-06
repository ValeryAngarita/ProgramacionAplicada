import matplotlib.pyplot as plt
import numpy as np

componente = ['Zonal', 'Troncal', 'TransmiCable']
cantidad_pasajeros = [8500, 9846, 5084]

plt.bar(componente, cantidad_pasajeros, color='c')
plt.title("Cantidad de pasajeros por componente")
plt.xlabel("Componentes")
plt.ylabel("Cantidad pasajeros")
plt.grid(False)
plt.show()
