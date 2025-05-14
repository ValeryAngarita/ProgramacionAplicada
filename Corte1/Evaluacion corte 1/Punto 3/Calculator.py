#Clase para crear la calculadora
class Calculator:
    def __init__(self):
        pass  # Constructor vacío

    def add(self, a, b):  # Retorna la suma de a y b
        return a + b

    def subtract(self, a, b):  # Retorna la resta de a menos b
        return a - b

    def multiply(self, a, b):  # Retorna el producto de a por b
        return a * b

    def divide(self, a, b):  # Retorna la división de a entre b o un mensaje de error
        try:
            return a / b
        except ZeroDivisionError:
            return "Matemáticamente incorrecto"

    def modulo(self, a, b):  # Retorna el módulo de a entre b o un mensaje de error
        try:
            return a % b
        except ZeroDivisionError:
            return "Matemáticamente incorrecto"
