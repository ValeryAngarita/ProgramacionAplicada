import matplotlib.pyplot as plt
import numpy as np

ad = np.random.randint(10, 5001, size=50) #Límite superior EXCLUSIVO. Size --> cantidad de números.
ventas = ad*np.random.uniform(0.8,1.2,size=50)

plt.scatter(ad, ventas, color='c')
plt.title("Gastos publicitarios vs ventas")
plt.xlabel("Gastos publicitarios")
plt.ylabel("Ventas")
plt.grid(True)
plt.show()
