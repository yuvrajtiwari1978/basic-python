# Demonstrating all common list methods in Python without using functions

lst = []
n = int(input("Enter the number of elements to add to the list: "))
print("Enter the elements:")
for i in range(n):
    elem = input()
    lst.append(str(elem))

print("Original list:", lst)

# append (push equivalent)
lst.append("new_element")
print("After append('new_element'):", lst)

# extend
lst.extend(["extend1", "extend2"])
print("After extend(['extend1', 'extend2']):", lst)

# insert
lst.insert(1, "inserted_element")
print("After insert(1, 'inserted_element'):", lst)

# remove
if "new_element" in lst:
    lst.remove("new_element")
print("After remove('new_element'):", lst)

# pop (remove last element)
popped = lst.pop()
print("After pop():", lst)
print("Popped element:", popped)

# clear
temp_lst = lst.copy()
temp_lst.clear()
print("After clear():", temp_lst)

# index
Index_pos = lst.index("extend1") if "extend1" in lst else -1
print("Index of 'extend1':", Index_pos)

# count
count_extend1 = lst.count("extend1")
print("Count of 'extend1':", count_extend1)

# sort
temp_lst2 = lst.copy()
try:
    temp_lst2.sort()
    print("After sort():", temp_lst2)
except Exception as e:
    print("Sort error:", e)
    print("Make sure all elements are of the same type and comparable.")

# reverse
temp_lst3 = lst.copy()
temp_lst3.reverse()
print("After reverse():", temp_lst3)

# copy
lst_copy = lst.copy()
print("Copy of list:", lst_copy)
