# Bernabe, Aleckxis Kate V.
# BSCpE 1-4

# Import the UserInterface class from the user_interface module
from user_interface import UserInterface

# Create a main function to start the program
def main():
    # Create an instance of the UserInterface class
    ui = UserInterface()

    while True:
        ui.get_operation()
        ui.get_numbers()

# Call the main function to start the program
if __name__ == "__main__":
    main()