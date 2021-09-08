import doctest
def is_sorted(n):
    """
    >>> is_sorted(2)
    True
    >>> is_sorted(22222)
    True
    >>> is_sorted(9876543210)
    True
    >>> is_sorted(9087654321)
    False
    """
    while n >= 10:
        last_digit = n%10
        n = n//10
        last_second_digit = n%10
        if last_digit > last_second_digit:
            return False    
    return True


def mario_number(level):
    """
    Return the number of ways that Mario can traverse the
    level, where Mario can either hop by one digit or two
    digits each turn. A level is defined as being an integer
    with digits where a 1 is something Mario can step on and 0
    is
    something Mario cannot step on.
    >>> mario_number(10101)
    1
    >>> mario_number(11101)
    2
    >>> mario_number(100101)
    0
    """
    def trees(label,k):
        if label ==1:
            return 1
        elif label%10 == 1 and label%100 ==11:
            return trees(label//10,k) + trees(label//100,k)
        elif label%100 ==11:
            return trees(label//100,k)
        elif label%10 ==1:
            return trees(label//100,k)
        else:
            return 0
    return trees(level,1)

def make_change(n):
    """"
    >>> make_change(5)
    2
    >>> make_change(6)
    2
    """
    if n <1:
        return 0
    elif n ==1 or n==3 or n==4:
        return 1
    elif n ==2 or n==5 or n==6 or n==7 or n==8:
        return 2    
    elif n%4==0:
        return n/4
    else:
        return (n+4)//4

def elephant(name, age, can_fly):
    """
    Takes in a string name, an int age, and a boolean can_fly.
    Constructs an elephant with these attributes.
    >>> dumbo = elephant("Dumbo", 10, True)
    >>> elephant_name(dumbo)
    "Dumbo"
    >>> elephant_age(dumbo)
    10
    >>> elephant_can_fly(dumbo)
    True
    """
    return [name, age, can_fly]

def elephant_name(e):
    return e[0]

def elephant_age(e):
    return e[1]

def elephant_can_fly(e):
    return e[2]


def elephant_roster(elephants):
    
    return [elephant_name(i) for i in elephants]

small = elephant('ss', 10 ,True)
middle = elephant('mm', 20 ,False)
big = elephant('bb', 30 ,True)
elephants = [small, middle, big]

a = elephant_roster(elephants)
