""" Lab 3: Recursion and Midterm Review """

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if b > a:
        return gcd(b,a) 
    elif a > b and a%b !=0:
        return gcd(b, a%b)
    elif a%b ==0:
        return b
    else:
        return 1


num = 1    
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    
    print(n)
    global num
    
    if n != 1:
        num +=1
        if n%2 == 1:
            hailstone(3*n+1)            
        else:
            hailstone(n//2)
              
    return num

from operator import add
def double(x):
    return x+ x
def square(y):
    return y*y
def f(z):
    add(square(double(z)),1)


