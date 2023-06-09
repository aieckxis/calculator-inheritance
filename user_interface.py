# Define UserInterface class
class UserInterface:
    def __init__(self):
        self.operation = ""
        self.num1 = 0
        self.num2 = 0

    # Ask the user for the operation to perform
    def get_operation(self):
        while True:
            self.operation = input("Please choose a math operation (+, -, *, /, power): ")
            if self.operation in ("+", "-", "*", "/", "**", "power"):
                break
            else:
                print("Error: Invalid operation.")

    # Ask the user for two numbers
    def get_numbers(self):
        while True:
            try:
                self.num1 = float(input("Enter the first number: "))
                self.num2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Error: Invalid input. Please enter a number.")

    # Calculate the result based on the chosen operation
    def calculate_result(self):
        if self.operation == "+":
            self.result = self.num1 + self.num2
        elif self.operation == "-":
            self.result = self.num1 - self.num2
        elif self.operation == "*":
            self.result = self.num1 * self.num2
        elif self.operation == "/":
            try:
                if self.num2 == 0:
                    raise ZeroDivisionError("Error: Cannot divide by zero.")
            except ZeroDivisionError as e:
                print(f"{str(e)} Please enter a second number again.")
                self.num2 = float(input("Enter the second number: "))
            self.result = self.num1 / self.num2
        elif self.operation == "power":
            self.result = self.num1 ** self.num2

    # Print the result

    def print_result(self):
        print("Result:", self.result)
