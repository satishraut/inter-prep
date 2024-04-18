
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return  number * factorial(number - 1)
#print(factorial(5))

def fib(n):
    """
    This function returns the nth Fibonacci number.
    The Fibonacci sequence is a series of numbers in which each number (after the first two) 
    is the sum of the two preceding"""
    #The first two numbers in the Fibonacci sequence are defined as 0 and  1
    #Every subsequent number in the sequence is the
    #sum of the two preceding ones, usually starting with 0 and 1
    
    if n <= 0:
        print("Input must be a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0,  1
        for i in range(2, n):
            a, b = b, a + b
        return b
        
print(fib(10))