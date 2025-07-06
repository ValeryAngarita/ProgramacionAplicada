import csv
import matplotlib.pyplot as plt
import numpy as np

# Leer los datos desde el archivo CSV (formato: latitud,longitud)
filename = 'datos_polares.csv'
angles = []
radii = []

# Leer datos GPS (lat, lon) desde el CSV
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = [list(map(float, row)) for row in reader if len(row) >= 2]

if len(data) < 2:
    print("No hay suficientes datos GPS en el archivo CSV.")
    exit()

# Primer punto como referencia
lat0, lon0 = data[0]
if lon0 > 0:
    lon0 = -lon0

# Convertir a coordenadas polares relativas
for lat, lon in data:
    if lon > 0:
        lon = -lon

    dlat = (lat - lat0) * 111000  # metros aproximados en dirección N-S
    dlon = (lon - lon0) * 111320 * np.cos(np.radians(lat0))  # metros en dirección E-O
    dist = np.sqrt(dlat**2 + dlon**2)
    angle = np.arctan2(dlat, dlon)
    angles.append(angle)
    radii.append(dist + 1.0)  # Separar visualmente los puntos

# Graficar
fig = plt.figure(figsize=(8, 8))  # Aumentar tamaño del gráfico
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, radii, 'o-', label='Trayectoria GPS')

# Agregar etiquetas con el número de punto, sin superposiciones
for i, (angle, radius) in enumerate(zip(angles, radii)):
    offset = 0.4 + 0.1 * (i % 2)  # Alterna la distancia de la etiqueta
    ax.text(angle, radius + offset, str(i + 1), fontsize=10, ha='center', va='center',
            bbox=dict(boxstyle="circle,pad=0.3", fc="white", ec="black", lw=0.5))

ax.set_title('Gráfico de coordenadas polares desde GPS')
ax.legend()
plt.show()
