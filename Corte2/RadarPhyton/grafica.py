import warnings
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import serial.tools.list_ports

matplotlib.use('TkAgg')

esp32_ports = [p.device for p in serial.tools.list_ports.comports() if 'USB' in p.description or 'ESP32' in p.description]
if not esp32_ports:
    raise IOError("No ESP32 port found")
print("ESP32 port found")

esp32_data = serial.Serial(esp32_ports[0], baudrate=115200)
esp32_data.flushInput()

fig = plt.figure("ESP32 Radar Scanner", facecolor='black')
ax = fig.add_subplot(111, polar=True, facecolor="#590430")
ax.set_ylim([0.0, 100])
ax.set_xlim([0.0, np.pi])
ax.set_thetagrids(np.linspace(0.0, 180.0, 7), color='pink')
ax.tick_params(axis='both', colors='pink')
ax.grid(True, which='major', linestyle='-', alpha=0.5, color='pink')
ax.text(np.pi/2, 140, "Radar ESP32 Valery y Juan", fontsize=16, color="#dc006e", ha='center', va='center')

points, = ax.plot([], linestyle='', marker='o', color='pink', markersize=5)
line, = ax.plot([], color='pink', linewidth=2)

angles = np.arange(0, 181, 1)
theta = angles * (np.pi / 180.0)
distances = np.zeros((len(angles),))

plt.show(block=False)

while True:
    while esp32_data.in_waiting == 0:
        pass
    esp32_string = esp32_data.readline()
    try:
        decoded = esp32_string.decode('utf-8').strip()
        print(f"Datos recibidos: {decoded}")
        parts = decoded.split(',')
        if len(parts) != 2:
            continue
        angle, distance = map(float, parts)
        if 0 <= angle <= 180:
            distances[int(angle)] = distance if distance <= 100 else 0
            points.set_data(theta, distances)
            line.set_data([angle * (np.pi / 180.0), angle * (np.pi / 180.0)], [0, 100])
            ax.figure.canvas.draw()
            ax.figure.canvas.flush_events()
    except:
        continue
