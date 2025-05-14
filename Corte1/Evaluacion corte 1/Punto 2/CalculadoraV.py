#Calculadora con programación Orientada a Objetos con un único
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

def main():
    my_calculator = Calculator() #sirve para crear una instancia (objeto) de la clase Calculator

    a = 10
    b = 0  # Cambia este valor para probar sin error

    print("Suma:", my_calculator.add(a, b))
    print("Resta:", my_calculator.subtract(a, b))
    print("Multiplicación:", my_calculator.multiply(a, b))
    print("División:", my_calculator.divide(a, b))
    print("Módulo:", my_calculator.modulo(a, b))

if __name__ == "__main__":
    main()
