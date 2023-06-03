# Define a function to ask the user if they want to try again
def ask_try_again():
    while True:
        try_again = input("Do you want to try again? (y/n): ").lower()
        if try_again in ["y", "n"]:
            return try_again
        else:
            print("Invalid input. Please enter 'y' to try again or 'n' to exit.")