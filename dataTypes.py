
# Basic Data Types And Advanced Datatypes

'''
 Basic Datatypes: Those datatypes stored only value at the time called basic data-types
    1) int(): Whole number
    2)float:  Number with a decimal point
    3)string(): order squence of charcter 'hello','test'
    4)complex(): it consists of two parts one-real part and another is imaginary part ex. a = 1+2j
    5)Bool(): stored the Boolean value it's True or False
'''

'''
Advanced Datatypes : Stored collections of values
1) List: Enclosed with in the square [] brackets ordered type by using index number we can access the value, mutable stores the value two blog of memory
2) Tuple: Enclosed by using the () parenthesis, faster than list, stored single memory of block
3) Dictionary: Enclosed with in the {} curly braces key and value pair, by using the key we can the access value
               but not vice-versa. order sequence is maintained.
4) set : Duplicate not allowed, enclosed with in {} braces, mutable datatypes empty set should be declared as
         abc=set()
5) frozonset: immutable form of set
'''

a = (10,20,30)
b = [10,20,30]
dic1={10:'ten', 20:'twenty',30:'thirty',40:'fourty'}

print(a[1])
print(b[1])
print(dic1)
# print(dic1[1]) Not allowed

abcd=set()
print(type(abcd))
fs = frozenset(['ten','twntye','pake','ten'])

print(fs, type(fs))
