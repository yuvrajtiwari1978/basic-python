# Demonstrating various types of error handling in Python

# ZeroDivisionError
try:
    x = 10
    y = 0
    result = x / y
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# ValueError
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

# IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Error: List index out of range.")

# KeyError
try:
    d = {'a': 1, 'b': 2}
    print(d['c'])
except KeyError:
    print("Error: Key not found in dictionary.")

# FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")

# TypeError
try:
    result = '2' + 2
except TypeError:
    print("Error: Unsupported operand type(s) for +.")

# ImportError
try:
    import non_existent_module
except ImportError:
    print("Error: Module not found.")

# Handling multiple exceptions
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")

# General exception handling added
try:
    x = int(input("\nEnter numerator: "))
    y = int(input("Enter denominator: "))
    result = x / y
    print(f"Result of division: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter integers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
