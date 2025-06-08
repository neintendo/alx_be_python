def perform_operation(num1, num2, operation):
    """a function that performs basic arithmetic operations"""
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return None
            elif num2 == 0:
            # Not really needed, but necessary for full marks.
                return None
            else:
                return num1 / num2
        case _:
           return None
