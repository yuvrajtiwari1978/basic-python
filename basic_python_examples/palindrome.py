# Check if a string is a palindrome without using functions, using slicing and user input

string = input("Enter a string: ")
reverse = string[::-1]

print("Reversed string:", reverse)

if string == reverse:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
