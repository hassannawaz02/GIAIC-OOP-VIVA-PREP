# Calculator class to perform basic arithmetic operations
class Calculator:
    def __init__(self, num1, num2):
        # Initialize the two numbers
        self.num1 = num1
        self.num2 = num2

    def add(self):
        # Return the sum of num1 and num2
        return self.num1 + self.num2

    def subtract(self):
        # Return the difference of num1 and num2
        return self.num1 - self.num2

    def multiply(self):
        # Return the product of num1 and num2
        return self.num1 * self.num2

    def divide(self):
        # Return the division of num1 by num2, handling division by zero
        if self.num2 == 0:
            return "Cannot divide by zero"
        else:
            return self.num1 / self.num2


# Example usage
calc1 = Calculator(10, 5)

print("Addition:", calc1.add())             # Output: 15
print("Subtraction:", calc1.subtract())     # Output: 5
print("Multiplication:", calc1.multiply())  # Output: 50
print("Division:", calc1.divide())           # Output: 2.0

print()

calc2 = Calculator(10, 0)
print("Division with zero:", calc2.divide())  # Output: Cannot divide by zero
