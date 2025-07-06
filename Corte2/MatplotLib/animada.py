import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
linea, = ax.plot(x, y)

def actualizar(frame):
    linea.set_ydata(np.sin(x + frame / 10))
    return linea,

ani = animation.FuncAnimation(fig, actualizar, frames=range(100), blit=True)
plt.show()
