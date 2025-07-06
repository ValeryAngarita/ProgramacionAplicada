import matplotlib.pyplot as plt
import numpy as np

zonas = ['Norte', 'Sur', 'Este', 'Oeste']
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
         'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
asistencias = np.random.randint(100, 2000, size=(4, 12))

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('Asistencia Mensual por Zona')

for i, zona in enumerate(zonas):
    ax = axs[i // 2, i % 2]
    ax.plot(meses, asistencias[i], marker='o')
    ax.set_title(zona)
    ax.set_xlabel("Mes")
    ax.set_ylabel("Asistencia (Personas)")

plt.tight_layout()
plt.show()
