# Demonstrating class, methods, constructor, object, and class variable in Python

class Person:
    # Class variable
    species = "Homo sapiens"

    # Constructor
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    # Method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    # Method to display species
    def display_species(self):
        print(f"I belong to the species {Person.species}")

# Taking input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Creating an object of the class
person1 = Person(name, age)

# Accessing methods
person1.greet()
person1.display_species()

# Accessing class variable directly
print("Class variable species:", Person.species)
