# Demonstrating the use of *args and **kwargs in Python functions

# Using *args to accept variable number of positional arguments
def print_args(*args):
    print("Positional arguments:")
    for arg in args:
        print(arg)

print_args(1, 2, 3, "four")

# Using **kwargs to accept variable number of keyword arguments
def print_kwargs(**kwargs):
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_kwargs(name="Alice", age=30, city="New York")

# Using both *args and **kwargs together
def print_all_args(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_all_args(10, 20, name="Bob", job="Developer")
