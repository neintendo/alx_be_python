def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        print("The result of the division is ", end='')
        return result
    except ValueError:
        return("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        return("Error: Cannot divide by zero.")
