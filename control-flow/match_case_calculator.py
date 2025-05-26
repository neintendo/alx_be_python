"""
Match Case Calculator: a script that prompts the user to enter two numbers and select
                       an operation (addition, subtraction, multiplication, or division). 
                       The script will then perform the selected operation using a
                       Match Case statement and display the result.
"""

value1 = int(input("Enter the first number: "))
value2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print("The result is ", int(value1 + value2), ".", sep="")
    case "-":
        print("The result is ", int(value1 - value2), ".", sep="")
    case "*":
        print("The result is ", int(value1 * value2), ".", sep="")
    case "/":
        if value2 == 0:
            print("Cannot divide by zero.")
            quit()
        print("The result is ", int(value1 / value2), ".", sep="")
    case _:
        print("ERROR: Unsupported operator!")


    
