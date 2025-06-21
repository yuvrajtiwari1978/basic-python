# Demonstrating slicing in Python

# Slicing a string
string = input("Enter a string: ")
print("Original string:", string)

start = int(input("Enter start index for slicing: "))
end = int(input("Enter end index for slicing: "))
step = int(input("Enter step for slicing: "))

sliced_string = string[start:end:step]
print("Sliced string:", sliced_string)

# Slicing a list
lst = []
n = int(input("Enter the number of elements in the list: "))
print("Enter the elements:")
for i in range(n):
    elem = input()
    lst.append(elem)

print("Original list:", lst)

start = int(input("Enter start index for list slicing: "))
end = int(input("Enter end index for list slicing: "))
step = int(input("Enter step for list slicing: "))

sliced_list = lst[start:end:step]
print("Sliced list:", sliced_list)
