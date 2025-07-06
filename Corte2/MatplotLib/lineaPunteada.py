import matplotlib.pyplot as plt
import numpy as np

meses = np.arange(1,50)
ventas = np.random.randint(2000, 4000, size = len(meses))
plt.plot(meses, ventas, color='blue',linestyle="--",marker='o')
plt.title("Venta de un producto por mes")
plt.xlabel("Mes")
plt.ylabel("Venta")
plt.grid(True)
plt.show()
