class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        result = self.num1 + self.num2
        return result

    def rem(self):
        result = self.num1 - self.num2
        return result

    def mul(self):
        result = self.num1 * self.num2
        return result

    def div(self):
        try:
            result = self.num1 / self.num2
            return result
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")
            return None