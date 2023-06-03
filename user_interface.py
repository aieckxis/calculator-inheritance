# Define UserInterface class
class UserInterface:
    def __init__(self):
        self.operation = ""
        self.num1 = 0

    # Ask the user for the operation to perform
    def get_operation(self):
        while True:
            self.operation = input("Please choose a math operation (+, -, *, /): ")

    # Ask the user for two numbers
    def get_numbers(self):
        while True:
            try:
                self.num1 = float(input("Enter the first number: "))
                self.num2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Error: Invalid input. Please enter a number.")