# Functions, Data Structures & Modules.

### arithmetic_operations.py

- *a function that performs basic arithmetic operations.*

- Parameters: num1 (float), num2 (float), and operation (string). The operation parameter accepts four possible values: 'add', 'subtract', 'multiply', or 'divide'.
- The function can execute the arithmetic operation based on the operation parameter and the numerical values provided.
- For division, it includes handling for division by zero, returning a specific message or value that the main.py script can recognize and display appropriately.
- Returns the result of the arithmetic operation. 

### shopping_list_manager.py

- *a script that implements a simple interface for managing a shopping list.*

##### Core Functionality:
- Starts with an empty list named shopping_list.
- Functionality to add items to the list, remove items, and display the current list.

##### User Interface:

- Uses a loop to continuously display a menu with options to the user until they choose to exit. 
  The menu offers options to add an item, remove an item, view the list, and exit.
- For adding items, it prompts the user for the item name and append it to shopping_list.
- For removing items, it asks the user for the item name and remove it from shopping_list. If the item is not found, it displays a message indicating so.
- To view the list, it prints each item in shopping_list to the console.
- Handles invalid menu choices gracefully.

### explore_datetime.py

- a script that performs specified operations with dates and times.

### temp_conversion_tool.py

- *a script that converts temperatures between Celsius and Fahrenheit, using global variables to store conversion factors.*

- Prompts the user to enter a temperature and specify whether it’s in Celsius or Fahrenheit.
- Based on the user’s input, it will call the appropriate conversion function and display the converted temperature.
- If the user entered a wrong input, it should raise an error that says: “Invalid temperature. Please enter a numeric value.”
