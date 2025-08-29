# AAL_Logic.py

from AAL_Functions import *

Flag = True

operations = {
    'A': add,
    'D': subtract,
    'M': multiply,
    'S': divide
}

def parse_operations_string(operations_string):
    # Split by '=' and flatten the list
    ops = []
    for part in operations_string.split('='):
        part = part.strip()
        if part:
            ops.extend(list(part))
    return ops

def process_input(operations_string, values_string, last_result):
    # Split the values into pairs
    value_parts = values_string.split('|')

    # Filter out '=' from operations_string for matching with value_parts
    filtered_operations = [op for op in operations_string if op != '=']

    # Iterate through each operation and corresponding value pair
    for i, operation in enumerate(filtered_operations):
        if i < len(value_parts):
            # Strip whitespace and split the numbers
            numbers = value_parts[i].strip().split(',')
            if len(numbers) == 1:  # If only one number is provided
                num1 = last_result  # Use the last result as the first number
                num2 = int(numbers[0])  # Convert the second number to integer
            elif len(numbers) == 2:  # If two numbers are provided
                num1, num2 = map(int, numbers)  # Convert string numbers to integers
            else:
                print(f"Error: Invalid number of values for operation '{operation}'")
                continue

            # Perform the operation
            if operation in operations:
                result = operations[operation](num1, num2)
                print(f"Result of {operation}({num1}, {num2}) = {result}")
                last_result = result  # Update last_result with the current result
            else:
                print(f"Error: Invalid operation '{operation}'")
        else:
            print(f"Error: Not enough value pairs for operation '{operation}'")

    return last_result  # Return the last result for further calculations

last_result = 0  # Initialize last_result

while Flag:
    # Example inputs
    operations_string = input("A = Addition, D = Subtraction, M = Multiplication, S = Division. Esc = exit \nEnter operations (e.g., AAD): ")
    operations_string = operations_string.upper()
    if operations_string == "ESC":
        quit()
    values_string = input("Enter values (e.g., 2,3|3,9|8,4): ")
    operations_string = operations_string.upper()
    values_string = values_string.upper()

    last_result = process_input(operations_string, values_string, last_result)
    print("------------------------------------------------------------------------------------------------")
