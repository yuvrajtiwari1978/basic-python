# Demonstrating if, else, elif statements in Python

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# Another example
age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age >= 13 and age < 20:
    print("Teenager")
else:
    print("Adult")
