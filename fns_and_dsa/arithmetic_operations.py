def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    if operation == "substract":
        return num1 - num2
    if operation == "multiply":
        return num1 * num2
    if operation == "divide":
        if num2 == '0':
            return "Error: Invalid division"
        else:
            return num1 / num2
    else:
        return "Invalid Operation"

