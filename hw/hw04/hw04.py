HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    "*** YOUR CODE HERE ***"
    return abs(street(a)-street(b))+abs(avenue(a)-avenue(b))

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    # i , j = 0, 0;
    # length = len(s);
    # while i <= length-1:
    #     if (s[i]**(1/2)) != round(s[i]**(1/2)):
    #         del s[i]
    #         length -=1            
    #     else:
    #         s[i] = int(s[i]**(1/2))
    #         i +=1    
    # return s    
    return([round(n**0.5) for n in s if round(n**0.5) == n**0.5])
    
    

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n ==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 3
    return g(n-1)+2*g(n-2)+3*g(n-3)
    

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n ==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 3
    else:
        total, i = 0, 4
        g1, g2, g3 =1,2,3
        while i <= n:
            total = 3*g1+2*g2+g3
            g1, g2, g3 = g2, g3, total
            i +=1        
        
    return total

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 7 == 0:
        return True
    elif k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # value, k, sign = 1, 1, 1
    # while k < n:
    #     if (has_seven(k)):                                     
    #         sign *=-1
    #         value, k = value+sign, k+1            
    #     else:
    #         value, k = value+sign, k+1           
    # return value

    def renew(value,k,sign):
        while k<n:       
            if (has_seven(k)):                                                     
                return renew(value-sign, k+1,-sign)            
            else:
                return renew(value+sign, k+1,sign)
        return value   
               
    return renew(1,1,1)
        

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    threshold, k = amount, 0
    while threshold>1:
        threshold *=0.5
        k +=1
        
    def count_partitions(amount,k):
        if amount <0:
            return 0                    
        elif amount ==1 or 0:
            return 1
        elif k ==0:
            return 1
        elif amount ==2:
            return 2
        else:
            return count_partitions(amount-pow(2,k), k) + count_partitions(amount,k-1)
    
    
    return count_partitions(amount,k)
    
###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return lambda n: (lambda f,n:f(f,n))(lambda s,x:x*s(s,x-1)if x>0 else 1,n)