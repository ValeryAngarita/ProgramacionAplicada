import matplotlib.pyplot as plt
import numpy as np

semanas = np.arange(10)
grupo1 = np.random.randint(50, 100, size=10)
grupo2 = grupo1 + np.random.randint(-5, 5, size=10)

# Gráfica con eje Y truncado
plt.plot(semanas, grupo1, label='Grupo 1')
plt.plot(semanas, grupo2, label='Grupo 2')
plt.ylim(90, 100)
plt.title("Aprobación con Eje Y Truncado")
plt.xlabel("Semana")
plt.ylabel("Porcentaje de Aprobación")
plt.legend()
plt.show()

# Gráfica con eje Y completo
plt.plot(semanas, grupo1, label='Grupo 1')
plt.plot(semanas, grupo2, label='Grupo 2')
plt.title("Aprobación con Eje Y Completo")
plt.xlabel("Semana")
plt.ylabel("Porcentaje de Aprobación")
plt.legend()
plt.show()
