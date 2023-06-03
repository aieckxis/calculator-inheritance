# Bernabe, Aleckxis Kate V.
# BSCpE 1-4

# Import the UserInterface, ExtendedUserInterface, and ask_try_again class
# from the user_interface, extended_user_interface, and try_again py files respectively.
from user_interface import UserInterface
from extended_user_interface import ExtendedUserInterface
from try_again import ask_try_again

# Create instances of UserInterface and ExtendedUserInterface
def main():
    ui = UserInterface()
    eui = ExtendedUserInterface()

    # Loop
    while True:
        # Get the operation and numbers from the user using ExtendedUserInterface
        eui.get_operation()
        eui.get_numbers()

        # Calculate and print the result using ExtendedUserInterface
        eui.calculate_result()
        eui.print_result()

        # Ask the user if they want to try again using ask_try_again function from try_again.py
        try_again = ask_try_again()
        # Break out of the loop if the user chooses not to try again
        if try_again == "n":
            print("Okay, thank you!")
            break

# Call the main function to start the program
if __name__ == "__main__":
    main()