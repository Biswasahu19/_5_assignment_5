class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return f"addition of {self.num1} and {self.num2} is : {self.num1 + self.num2}"
    def subtract(self):
        return f"subtraction {self.num1} and {self.num2} is : {self.num1 - self.num2}"
    def multiply(self):
        return f"multiplation {self.num1} and {self.num2} is: {self.num1 * self.num2}"
    def divide(self):
        return f"division {self.num1} and {self.num2} is    : {self.num1 / self.num2}"

calculator_obj = Calculator(34,9)
print(calculator_obj.add())
print(calculator_obj.subtract())
print(calculator_obj.multiply())
print(calculator_obj.divide())
