# Demonstrating list vs set vs tuple in Python

# List: ordered, mutable, allows duplicates
my_list = []
n = int(input("Enter the number of elements for the list: "))
print("Enter elements for the list:")
for i in range(n):
    elem = input()
    my_list.append(elem)
print("List:", my_list)

# Set: unordered, mutable, no duplicates
my_set = set()
print("\nEnter elements for the set:")
for i in range(n):
    elem = input()
    my_set.add(elem)
print("Set:", my_set)

# Tuple: ordered, immutable, allows duplicates
my_tuple = ()
print("\nEnter elements for the tuple:")
temp_list = []
for i in range(n):
    elem = input()
    temp_list.append(elem)
my_tuple = tuple(temp_list)
print("Tuple:", my_tuple)

# Demonstrate some operations
print("\nAccessing elements:")
print("List first element:", my_list[0])
print("Tuple first element:", my_tuple[0])
# Sets do not support indexing

print("\nLength of each:")
print("List length:", len(my_list))
print("Set length:", len(my_set))
print("Tuple length:", len(my_tuple))
