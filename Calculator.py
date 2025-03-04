def calculator(num1, num2, operation):
    print("Simple Calculator")
    
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            result = num1 / num2
        else:
            return "Invalid operation. Please choose +, -, *, or /."
        
        return f"Result: {result}"
    except ValueError:
        return "Invalid input. Please enter numeric values."

# Example test cases
print(calculator(10, 5, '+'))  # Expected: 15
print(calculator(10, 5, '-'))  # Expected: 5
print(calculator(10, 5, '*'))  # Expected: 50
print(calculator(10, 5, '/'))  # Expected: 2.0
print(calculator(10, 0, '/'))  # Expected: Error: Division by zero is not allowed.
print(calculator(10, 5, 'x'))  # Expected: Invalid operation.
