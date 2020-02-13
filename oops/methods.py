'''
Function: it is defined outside the class called function, it is a set of instructions
Method: Declared inside the class
Types of methods:
1) Instance Method: Object Level method
2)Static Methods: No way related to the class we can use for the unique logic
3)class Method: Access the class level variable
'''

class MyClass:
    clsVariable = 'my class variable'

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self)

    @classmethod
    def testing(cls):
        print(cls.clsVariable)

    @staticmethod
    def multiplication(a, b):
        print(a*b)

obj1=MyClass('satish',11)
print(obj1)
obj1.testing()

obj1.multiplication(10,10)