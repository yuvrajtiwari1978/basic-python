# Demonstrating nested lists and accessing elements in nested lists

# Creating a nested list
nested_list = [
    [1, 2, 3],
    ['a', 'b', 'c'],
    [True, False, True]
]

print("Nested list:")
print(nested_list)

# Accessing elements in nested list
print("\nAccessing elements:")
print("First element of first list:", nested_list[0][0])
print("Second element of second list:", nested_list[1][1])
print("Third element of third list:", nested_list[2][2])

# Iterating through nested list
print("\nIterating through nested list:")
for i in range(len(nested_list)):
    for j in range(len(nested_list[i])):
        print(f"Element at [{i}][{j}]:", nested_list[i][j])
