import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

def on_click(event): #Esta función es llamada al hacer clic en el plot
    print(f"Se hizo clic en las coordenadas: ({event.xdata}, {event.ydata})")

fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()
