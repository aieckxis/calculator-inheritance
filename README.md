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
