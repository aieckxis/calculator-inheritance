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
        ui.calculate_result()
        ui.print_result()

        # Ask the user if they want to try again
        try_again = input("Do you want to try again? (y/n): ").lower()
        if try_again == "n":
            print("Okay, thank you!")
            break

# Call the main function to start the program
if __name__ == "__main__":
    main()