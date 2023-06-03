# Define MathOperations class
class UserInterface:
    def __init__(self):
        self.operation = ""
        self.num1 = 0

    # Ask the user for the operation to perform
    def get_operation(self):
        while True:
            self.operation = input("Please choose a math operation (+, -, *, /): ")