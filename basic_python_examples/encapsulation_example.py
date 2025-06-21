# Demonstrating encapsulation, protected and private variables, and name mangling in Python

class EncapsulationExample:
    def __init__(self):
        self.public_var = "I am public"
        self._protected_var = "I am protected"
        self.__private_var = "I am private"

    def show_vars(self):
        print("Public variable:", self.public_var)
        print("Protected variable:", self._protected_var)
        print("Private variable:", self.__private_var)

    def get_private_var(self):
        return self.__private_var

obj = EncapsulationExample()

# Accessing variables
print(obj.public_var)          # Public access
print(obj._protected_var)      # Protected access (convention)
# print(obj.__private_var)     # This will raise an AttributeError

# Accessing private variable using name mangling
print(obj._EncapsulationExample__private_var)

# Using method to access private variable
print(obj.get_private_var())

# Showing all variables using method
obj.show_vars()
