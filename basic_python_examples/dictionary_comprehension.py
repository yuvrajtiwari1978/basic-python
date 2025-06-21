# Demonstrating dictionary and dictionary comprehension in Python

# Creating a dictionary
d = {}
n = int(input("Enter the number of key-value pairs: "))
print("Enter the key-value pairs:")
for _ in range(n):
    key = input("Key: ")
    value = input("Value: ")
    d[key] = value

print("Dictionary:")
print(d)

# Accessing dictionary elements
print("\nAccessing elements:")
for key in d:
    print(f"Key: {key}, Value: {d[key]}")

# Dictionary comprehension: create a dictionary with keys as numbers and values as their squares
num_dict = {x: x**2 for x in range(1, 6)}
print("\nDictionary comprehension (number: square):")
print(num_dict)
