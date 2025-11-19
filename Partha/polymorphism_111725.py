class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        print("The Sum is :", self.a + self.b)

    def sub(self):
        print("The Subtraction is :", self.a - self.b)

    def mult(self):
        print("The Multiplication is :", self.a * self.b)

    def div(self):
        print("The Division is :", self.a / self.b)

class Scientific_Calc(Calculator):
    def __init__(self, a, b):