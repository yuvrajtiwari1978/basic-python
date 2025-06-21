# Demonstrating list and list comprehension in Python

# Creating a list
numbers = []
n = int(input("Enter the number of elements in the list: "))
print("Enter the elements:")
for i in range(n):
    elem = int(input())
    numbers.append(elem)

print("Original list:", numbers)

# List comprehension to create a list of squares
squares = [x**2 for x in numbers]
print("List of squares using list comprehension:", squares)

# List comprehension with condition (even numbers)
evens = [x for x in numbers if x % 2 == 0]
print("List of even numbers using list comprehension:", evens)
