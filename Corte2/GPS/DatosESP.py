import machine
import time

# Configura el UART para comunicarte con el GPS
uart = machine.UART(2, baudrate=9600, tx=17, rx=16)  # Cambia los pines si es necesario

# Función para convertir coordenadas NMEA a decimal
def nmea_to_decimal(coord, direction):
    degrees = int(float(coord) / 100)
    minutes = float(coord) - degrees * 100
    decimal = degrees + minutes / 60
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal

# Bucle principal
while True:
    if uart.any():
        line = uart.readline()
        try:
            line = line.decode('utf-8')
            if line.startswith('$GPGLL'):
                parts = line.split(',')
                if len(parts) >= 5 and parts[1] and parts[3]:
                    lat = nmea_to_decimal(parts[1], parts[2])
                    lon = nmea_to_decimal(parts[3], parts[4])
                    print("{:.6f},{:.6f}".format(lat, lon))
        except Exception as e:
            pass  # Ignora errores de decodificación o de datos
    time.sleep(1)
