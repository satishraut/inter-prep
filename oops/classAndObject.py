'''
What is class?: class is a container or it is a templates, by using the class we can create multible objest
What is object: Object is a real world entity. it has some attributes and features
'''

'''
If we unsure about the what elements get passed then we can use the *args and **kwargs
*args : Argument without keyword
**kwargs: keyword arguments with keyword
'''

class MyClass:
    def __init__(self, *args, **kwargs): # constructor automaticaly called when objects get created not required memorySpace
        self.name = kwargs
        self.age = args
        self.roll=kwargs

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)


obj = MyClass('satish', 44,66,90)
print(obj)
