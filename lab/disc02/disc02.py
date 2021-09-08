# q1.1
from operator import add

six = 1


def ty(one, a):
    fall = one(a, six)
    return fall


six = ty(add, 6)
fall = ty(add, 6)

# q1.2


def curry2(h):
    def f(x):
        def g(y):
            return h(x, y)
        return g
    return f


make_adder = curry2(lambda x, y: x + y)
add_three = make_adder(3)
five = add_three(2)

# q1.3
n = 7


def f(x):
    n = 8
    return x+1


def g(x):
    n = 9

    def h():
        return x+1
    return h


def f(f, x):
    return f(x+n)


f = f(g, n)
g = (lambda y: y())(f)

# q1.4
y = "y"
h = y
def y(y):
    h = "h"
    if y == h:
        return y+"i"
    y = lambda y:y(h)
    return lambda h: y(h)

y = y(y)(y)

# q2.1

def multiply(m,n):
    if n>1:
        return m + multiply(m,n-1)
    return m

# q2.2

def countdown(n):  
    if n>0:
        print(n)
        return countdown(n-1)
    

# q2.4

def sum_digits(n):      
    if n>0:   
        return n%10 +sum_digits(n//10)
    return n//10
    
# q3.1

def count_stair_ways(n):
    if n ==1:
        return 1
    elif n==2:
        return 2
    if n>0: 
        return count_stair_ways(n-1)+count_stair_ways(n-2)

# q3.2
def count_k(n,k):
    if n<0:
        return 0
    elif n ==0:
        return 1
    else:
        i, total =1, 0;
        while i<=k:
            total += count_k(n-i,k)
            i +=1
        return total