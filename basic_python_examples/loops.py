# Demonstrating loops in Python

count_for = int(input("Enter the number of iterations for for loop: "))
print("For loop:")
for i in range(count_for):
    print(i)

count_while = int(input("\nEnter the number of iterations for while loop: "))
print("\nWhile loop:")
count = 0
while count < count_while:
    print(count)
    count += 1
