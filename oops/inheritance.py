'''Inheritance is powerful feature in object oriented programming. We can use methods and attributes of parent class
    into the child class:

    Types of Inheritance in python:
    1) Single Inheritance: one parent and one child class
    2) Multiple Inheritance: one child is having multiple parent classes
    3) Multilevel inheritance
    4) Hierarchical Inheritance: multiple child one parent,More than one derived classes are created from a single base.
'''

# Single Inheritance
class Parent:
    def parent_fun(self):
        return 'i am in parent class'

class Child(Parent):
    def child_fun(self):
        return 'i am in a child class'

child=Child()
print(child.parent_fun()) # By Using Child class we can dirctly access the parent method

# Multiple Inheritance
class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print
        "Base1"


class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")

class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printStrs()
# Multi Level Inheritance
class A:
    def inClassA(self,a=10):
        print('In class A')
class B(A):
    def inClassB(self):
        print('In class B')
class C(B):
    def inClassC(self):
        print('in class C')

c = C() # Object Created of class C

c.inClassA()
c.inClassB()
c.inClassC()

