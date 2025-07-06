import matplotlib.pyplot as plt
import numpy as np

resultados = np.random.normal(loc=70, scale=10, size=1000)
plt.boxplot(resultados)
plt.title("Diagrama de Caja de Resultados")
plt.ylabel("Puntajes")
plt.show()
