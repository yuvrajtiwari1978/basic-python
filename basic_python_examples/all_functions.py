# Demonstrating usage of various functions in Python except arithmetic functions

# User-defined function without parameters
def greet():
    print("Hello, World!")

greet()

# User-defined function with parameters
def add(a, b):
    return a + b

print("Sum of 5 and 3 is:", add(5, 3))

# User-defined function with default parameter
def power(base, exponent=2):
    return base ** exponent

print("Power of 4 squared is:", power(4))
print("Power of 2 cubed is:", power(2, 3))

# User-defined function with variable number of arguments
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print("Product of 2, 3, 4 is:", multiply(2, 3, 4))

# Using built-in functions except arithmetic ones
print("Length of 'Python' is:", len("Python"))
print("Maximum of [1, 5, 3] is:", max([1, 5, 3]))
print("Minimum of [1, 5, 3] is:", min([1, 5, 3]))
print("Sorted list of [3, 1, 2] is:", sorted([3, 1, 2]))
print("Type of 123 is:", type(123))
print("String representation of 123 is:", str(123))
print("Integer conversion of '456' is:", int("456"))
print("Float conversion of '3.14' is:", float("3.14"))
print("Boolean value of 0 is:", bool(0))
print("Boolean value of 1 is:", bool(1))
print("Character for ASCII 65 is:", chr(65))
print("ASCII code for 'A' is:", ord('A'))
print("Reversed list of [1, 2, 3] is:", list(reversed([1, 2, 3])))
print("Enumerate list ['a', 'b', 'c']:")
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)
print("Zip lists [1, 2, 3] and ['a', 'b', 'c']:")
for pair in zip([1, 2, 3], ['a', 'b', 'c']):
    print(pair)
