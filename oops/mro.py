''' Method Resolution Order Especially it plays vital role in the context of multiple inheritance as single method may be
found in multiple super classes '''

class A:
    def funInClassA(self):
        return 'i am in class A'

class B:
    def funInClassB(self):
        return 'i am in class B'

class C(A,B):
    def funInclassC(self):
        return 'i am in class C'

obj_c = C()

print(C.mro())
