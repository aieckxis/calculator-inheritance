# Object-Oriented Calculator with Inheritance in Python

This repository contains a Python script for an **interactive calculator program** that allows users to perform basic arithmetic operations that applies **inheritance**. It asks the user to enter an operation (+, -, *, /, power) and two numbers. The program then calculates the result and prints it. After each calculation, the user is asked if they want to try again. If they choose to try again, they can perform another calculation. If they choose not to try again, the program exits with a "Thank you!" message.

## Usage
Using Command Prompt: 

1. Open the Start menu and search for "Command Prompt".
2. Click on "Command Prompt" to open the command prompt window.
3. Use the cd command to navigate to the directory containing the script file. For example, if the script file is located in the "Documents" folder, type: cd Documents
4. Type the command python script_name.py to run the script. Replace "script_name.py" with the actual name of the **main** script file.
5. Press Enter to run the script.
6. The script will run and will display a prompt asking the user to choose a math operation (+, -, *, /, power).
7. The program will ask the user to enter two numbers.
8. The program will calculate the result based on the chosen operation and display it.
9. If the user attempt to divide by zero, an error message will be shown, and user will be asked to enter the second number again.
10. After displaying the result, the program will ask if the user want to try again.
11. If the user choose to try again, they can input a new operation and numbers.
12. The program will continue running until ther user choose to exit.

Alternatively, you can also run the script using the Python IDLE environment:

1. Open the Start menu and search for "Python".
2. Click on "Python" to open the Python IDLE environment.
3. Click on "File" at the top of the window and select "Open".
4. Navigate to the directory containing the **main** script file and select it.
5. Click on "Run" at the top of the window and select "Run Module" or press the F5 key.
6. The script will run and will display a prompt asking the user to choose a math operation (+, -, *, /, power).
7. The program will ask the user to enter two numbers.
8. The program will calculate the result based on the chosen operation and display it.
9. If the user attempt to divide by zero, an error message will be shown, and user will be asked to enter the second number again.
10. After displaying the result, the program will ask if the user want to try again.
11. If the user choose to try again, they can input a new operation and numbers.
12. The program will continue running until ther user choose to exit.

## Code Explanation
### — program.py

<img width="600" alt="image" src="https://github.com/aieckxis/calculator-inheritance/assets/129574374/4565040a-d0c6-4ae1-96b6-e8d2f1a3d47b">

The code begins by importing the **UserInterface**, **ExtendedUserInterface**, and **ask_try_again** classes from separate Python files (**user_interface.py**, **extended_user_interface.py**, and **try_again.py**).

<img width="600" alt="image" src="https://github.com/aieckxis/calculator-inheritance/assets/129574374/58154c35-f6eb-499a-a7e0-39dab212067e">

Next, the **main()** function is defined. Inside this function, instances of the **UserInterface** and **ExtendedUserInterface** classes are created and assigned to variables **ui** and **eui**, respectively.

<img width="600" alt="image" src="https://github.com/aieckxis/calculator-inheritance/assets/129574374/52f2ecf6-157a-4787-8cbe-0b8889fa5346">

The program enters a while **loop**, which allows the user to perform multiple calculations until they choose to exit. Within the loop, the program uses the **ExtendedUserInterface** to get the desired math operation and numbers from the user. The program then calculates the result based on the chosen operation using the **calculate_result()** method of **ExtendedUserInterface**. After calculating the result, the program prints it using the **print_result()** method of **ExtendedUserInterface**. The program asks the user if they want to try again by calling the **ask_try_again()** function from **try_again.py.** If the user chooses not to try again **(input 'n')**, the program breaks out of the loop and displays the message **"Okay, thank you!".**

<img width="600" alt="image" src="https://github.com/aieckxis/calculator-inheritance/assets/129574374/16fa0be6-6dcb-4ff6-826d-00f10b73d7ef">

Finally, the **main()** function is called to start the program if the script is executed directly.

### — user_interface.py

<img width="600" alt="image" src="https://github.com/aieckxis/calculator-inheritance/assets/129574374/1aa95142-764a-40e0-871f-8f69fd2fe881">

The **UserInterface** class is defined with an **_ _ init _ _** method. This method initializes the class attributes **operation**, **num1**, and **num2** to default values.

<img width="600" alt="image" src="https://github.com/aieckxis/calculator-inheritance/assets/129574374/95c7c0ce-8801-40b0-b412-868c12418167">

The **get_operation** method is defined to ask the user for the desired math operation. It uses a while loop to repeatedly ask for input until a valid operation is entered. The valid operations are +, -, *, /, and power.

<img width="600" alt="image" src="https://github.com/aieckxis/calculator-inheritance/assets/129574374/d5a489e0-bac3-4c0c-8f4d-3eeb16491f75">

The **get_numbers** method is defined to ask the user for two numbers. It uses a **try-except** block to handle invalid inputs and continues to ask for input until two valid numbers are entered.

<img width="600" alt="image" src="https://github.com/aieckxis/calculator-inheritance/assets/129574374/37e7c8cf-9c06-41b7-8a7b-5440e1095972">

The **calculate_result** method is defined to perform the calculation based on the chosen operation. It uses a series of conditional statements **(if, elif)** to determine the operation and perform the corresponding calculation. The result is stored in the result attribute of the class.

<img width="600" alt="image" src="https://github.com/aieckxis/calculator-inheritance/assets/129574374/d015ce8e-b4ff-472d-bd6c-62c4a246e135">

The **print_result** method simply prints the result to the console.

### — extended_user_interface.py

<img width="600" alt="image" src="https://github.com/aieckxis/calculator-inheritance/assets/129574374/7481e41f-3049-461f-806e-f22e23cad2a9">

Imports the **UserInterface** class from the **user_interface** module. It allows the **UserInterface** class to be used in the current module.

<img width="600" alt="image" src="https://github.com/aieckxis/calculator-inheritance/assets/129574374/ca46e870-87a8-4580-ae57-f59ef2bf39ee">

The **ExtendedUserInterface** class inherits from the **UserInterface** class by specifying **UserInterface** in parentheses after the class name. The **get_operation()** method is overridden to provide a custom implementation. It asks the user to choose a math operation by taking input from the user and validates the input to ensure it is one of the valid operations: "+", "-", "*", "/", or "power".

<img width="600" alt="image" src="https://github.com/aieckxis/calculator-inheritance/assets/129574374/356227ab-152f-4539-a3e0-c33db915cecb">

The **get_numbers()** method is also overridden to provide a custom implementation. It asks the user to enter the first and second numbers, and performs input validation to ensure that valid floating-point numbers are entered. If an invalid input is provided, an error message is displayed.

<img width="600" alt="image" src="https://github.com/aieckxis/calculator-inheritance/assets/129574374/d052f83a-33cd-4e3e-9438-3a1ef82c0b73">

The **calculate_result()** method overrides the parent class's method. It first checks if the chosen operation is division ("/") and if the second number is **zero**. If both conditions are met, it displays an error message indicating that division by zero is not allowed, asks the user to enter the second number again using the **get_numbers()** method, and returns from the method. If the conditions are not met, it calls the parent class's **calculate_result()** method using **super().calculate_result()** to perform the calculation based on the chosen operation.

<img width="600" alt="image" src="https://github.com/aieckxis/calculator-inheritance/assets/129574374/b36c75ef-345f-4dc5-a294-c2d7dea43347">

The **print_result()** method overrides the parent class's method. It calls the parent class's **print_result()** method using **super().print_result()** to print the calculated result.

### — try_again.py

<img width="600" alt="image" src="https://github.com/aieckxis/calculator-inheritance/assets/129574374/1c9539db-7bdb-418d-814a-6135a273196c">

The function is defined using the **def** keyword, followed by the function name **ask_try_again()**. It does not take any arguments and does not return any values.

<img width="600" alt="image" src="https://github.com/aieckxis/calculator-inheritance/assets/129574374/2eafc119-0672-4282-82dd-a60bc3c25576">

Within the function, there is a while **loop** that continues until a valid input is received from the user. This loop ensures that the user is asked repeatedly until they provide a valid response. Inside the **loop**, the user is asked with the question **"Do you want to try again? (y/n):"**. **The input()** function is used to capture the user's response, which is then converted to lowercase using the **.lower()** method. This conversion helps to make the comparison case-insensitive.

<img width="600" alt="image" src="https://github.com/aieckxis/calculator-inheritance/assets/129574374/1a7d9953-7198-46c0-bd1f-502ea7a6db58">

The user's input is then checked using an if statement to determine if it matches either **"y"** or **"n"**. If the input is valid, meaning it is either **"y"** or **"n"**, the function exits the loop using the **return** statement, and the user's response is returned as the result of the function. If the user enters an invalid input, any value other than **"y"** or **"n"**, an error message is displayed using the **print()** function. This informs the user that their input is invalid and prompts them to enter either **"y"** or **"n"** again. The function continues to loop until a valid input is provided by the user, ensuring that the program does not proceed until a valid choice is made.

