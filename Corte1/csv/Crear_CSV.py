import csv

datos = [
    ["Nombre", "Edad", "Ciudad"],
    ["Ana", 25, "Lima"],
    ["Luis", 30, "Bogotá"],
    ["María", 28, "Ciudad de México"]
]

with open("personas.csv", mode="w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)

print("CSV creado y datos escritos correctamente.")