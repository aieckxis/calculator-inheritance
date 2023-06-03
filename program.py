# Bernabe, Aleckxis Kate V.
# BSCpE 1-4

# Import the UserInterface class from the user_interface module
from user_interface import UserInterface
# Import the ExtendedUserInterface class from the extended_user_interface module
from extended_user_interface import ExtendedUserInterface

def main():
    ui = UserInterface()
    eui = ExtendedUserInterface()

    while True:
        eui.get_operation()
        eui.get_numbers()
        eui.calculate_result()
        eui.print_result()

        try_again = input("Do you want to try again? (y/n): ").lower()
        while try_again != "y" and try_again != "n":
            try_again = input("Invalid input. Please enter 'y' to try again or 'n' to exit: ").lower()

        if try_again == "n":
            print("Okay, thank you!")
            break

if __name__ == "__main__":
    main()