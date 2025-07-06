import matplotlib.pyplot as plt
import numpy as np

dias = np.arange(0, 10, 1)
actividad1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
actividad2 = np.array([5, 15, 10, 25, 20, 30, 25, 35, 30, 40])

# Gráfica de áreas solapadas (puede inducir a error)
plt.fill_between(dias, actividad1, color='skyblue', alpha=0.5)
plt.fill_between(dias, actividad2, color='orange', alpha=0.5)
plt.title("Gráfica de Área Potencialmente Confusa")
plt.xlabel("Día")
plt.ylabel("Asistencia")
plt.show()

# Gráfica mejorada con áreas apiladas sin solapamiento
plt.fill_between(dias, actividad1, color='skyblue', alpha=0.5)
plt.fill_between(dias, actividad1 + actividad2, actividad1, color='orange', alpha=0.5)
plt.title("Gráfica de Área Apilada Mejorada")
plt.xlabel("Día")
plt.ylabel("Asistencia")
plt.show()
