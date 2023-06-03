# Import the UserInterface class from the user_interface module
from user_interface import UserInterface

# Define ExtendedUserInterface class that inherits from UserInterface
class ExtendedUserInterface(UserInterface):
    def get_operation(self):
        while True:
            self.operation = input("Please choose a math operation (+, -, *, /, power): ")
            if self.operation in ("+", "-", "*", "/", "**", "power"):
                break
            else:
                print("Error: Invalid operation.")

    def get_numbers(self):
        while True:
            try:
                self.num1 = float(input("Enter the first number: "))
                self.num2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Error: Invalid input. Please enter a number.")

    def calculate_result(self):
        if self.operation == "/":
            if self.num2 == 0:
                print("Error: Cannot divide by zero.")
                self.get_numbers()
                return
        super().calculate_result() # Call the parent class's calculate_result() method

    def print_result(self):
        super().print_result() # Call the parent class's print_result() method