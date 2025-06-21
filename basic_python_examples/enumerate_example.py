# Demonstrating usage of enumerate in a for loop

items = []
n = int(input("Enter the number of items: "))
print("Enter the items:")
for i in range(n):
    item = input()
    items.append(item)

print("Items with their indices using enumerate:")
for index, value in enumerate(items):
    print(f"Index {index}: {value}")
