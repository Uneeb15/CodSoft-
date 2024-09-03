# Simple Calculator in Python

# Function to perform the calculation based on the operation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation."

# Prompt the user to input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Prompt the user to choose an operation
operation = input("Choose an operation (+, -, *, /): ")

# Perform the calculation and display the result
result = calculate(num1, num2, operation)
print(f"The result of {num1} {operation} {num2} is: {result}")
