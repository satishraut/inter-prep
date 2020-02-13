'''
Override means having two methods with the same name but doing different tasks.
 It means that one of the methods overrides the other.

 Like other languages (for example method overloading in C++) do, python does not supports method overloading.
 We may overload the methods but can only use the latest defined method.
'''

class Rectangle():
    def __init__(self, lentgh, breadth):
        self.lentgh = lentgh
        self.breadth = breadth

    def getArea(self):
        print(self.lentgh * self.breadth,"Is area of rectangle")

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        Rectangle.__init__(self,side,side)

    def getArea(self):
        print(self.side*self.side,"is area of square")

s = Square(4)
r = Rectangle(2,4)
s.getArea()
r.getArea()
