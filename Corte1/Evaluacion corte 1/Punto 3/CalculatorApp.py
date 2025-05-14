#Aplicativo para ejecutar la calculadora
from Calculator import Calculator  

class CalculatorApp:
    def __init__(self):
        self.calculator = Calculator()  

    def run(self):
        a = 10  #Valor a
        b = 0   #Valor b

        print("Suma:", self.calculator.add(a, b))
        print("Resta:", self.calculator.subtract(a, b))
        print("Multiplicación:", self.calculator.multiply(a, b))
        print("División:", self.calculator.divide(a, b))
        print("Módulo:", self.calculator.modulo(a, b))

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
