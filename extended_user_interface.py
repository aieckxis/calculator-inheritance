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

    # Override the get_numbers() method to ask for two numbers
    def get_numbers(self):
        while True:
            try:
                self.num1 = float(input("Enter the first number: "))
                self.num2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Error: Invalid input. Please enter a number.")

    # Override the calculate_result() method to include the two numbers in calculations
    def calculate_result(self):
        super().calculate_result()  # Call the parent class's calculate_result() method

    # Override the print_result() method
    def print_result(self):
        super().print_result()  # Call the parent class's print_result() method