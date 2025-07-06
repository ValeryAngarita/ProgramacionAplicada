import matplotlib.pyplot as plt
import numpy as np

empresas = ['Claro', 'Movistar', 'Tigo', 'WOM', 'ETB/AT&T']
distribucion = [40, 30, 20, 8, 2]

plt.pie(distribucion,labels=empresas, autopct='%1.1f%%', colors=['red', 'green', 'b', 'm','c'])
plt.title("Distribución espectro electomagnético para telefonía móvil \n en Colombia 2023")
plt.grid(False)
plt.show()
