# Demonstrating all kinds of inheritance in Python using Parent, Child, and Mother classes

# Single Inheritance
class Parent:
    def show_parent(self):
        print("This is the Parent class")

class Child(Parent):
    def show_child(self):
        print("This is the Child class")

# Multilevel Inheritance
class GrandChild(Child):
    def show_grandchild(self):
        print("This is the GrandChild class")

# Multiple Inheritance
class Mother:
    def show_mother(self):
        print("This is the Mother class")

class ChildWithMother(Parent, Mother):
    def show_child_with_mother(self):
        print("This is the Child class with Mother")

# Hierarchical Inheritance
class AnotherChild(Parent):
    def show_another_child(self):
        print("This is another Child class")

# Hybrid Inheritance (combination of multiple and multilevel)
class HybridChild(GrandChild, Mother):
    def show_hybrid_child(self):
        print("This is the Hybrid Child class")

# Testing the inheritance
parent = Parent()
parent.show_parent()

child = Child()
child.show_parent()
child.show_child()

grandchild = GrandChild()
grandchild.show_parent()
grandchild.show_child()
grandchild.show_grandchild()

mother = Mother()
mother.show_mother()

child_with_mother = ChildWithMother()
child_with_mother.show_parent()
child_with_mother.show_mother()
child_with_mother.show_child_with_mother()

another_child = AnotherChild()
another_child.show_parent()
another_child.show_another_child()

hybrid_child = HybridChild()
hybrid_child.show_parent()
hybrid_child.show_child()
hybrid_child.show_grandchild()
hybrid_child.show_mother()
hybrid_child.show_hybrid_child()
