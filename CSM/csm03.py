# 2

a = [1,2,[3]]
def mystery(s,t):
    s.pop(1)
    # print(s)    
    # print(t)
    # print(t.append(s))
    return t.append(s)

b = a
a += [b[0]]
a = mystery(b, a[1:])

# 3

def accumulate(lst):
    """
    >>> l = [1, 5, 13, 4]
    >>> accumulate(l)
    23
    >>> l
    [1, 6, 19, 23]
    >>> deep_l = [3, 7, [2, 5, 6], 9]
    >>> accumulate(deep_l)
    32
    >>> deep_l
    [3, 10, [2, 7, 13], 32]
    """
    sum = 0
    for i in range(len(lst)):
        inside = 0
        if isinstance(lst[i], list):
            inside = accumulate(lst[i])        
        else:
            inside = lst[i]         
            lst[i] = inside + sum
        sum += inside        
    return sum

    
# Nonlocality
# 1

eggplant = 8
def vegetable(kale):
    def eggplant(spinach):
        nonlocal eggplant
        nonlocal kale
        kale = 9
        eggplant = spinach
        print(eggplant, kale)
    eggplant(kale)
    return eggplant

# spinach = vegetable('kale')

# 2

def has_seven(k): # Use this function for your answer below
    if k % 7 == 0:
        return True
    elif k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)
def make_pingpong_tracker():
    """ Returns a function that returns the next value in the
    pingpong sequence each time it is called.
    >>> output = []
    >>> x = make_pingpong_tracker()
    >>> for _ in range(9):
    ... output += [x()]
    >>> output
    [1, 2, 3, 4, 5, 6, 7, 6, 5]
    """
    index, current, add = 1, 0, True
    def pingpong_tracker():
        nonlocal current,index,add
        if add:
            current += 1
        else:
            current -= 1
        if has_seven(index):
            add = not add
        index += 1
        return current
    return pingpong_tracker

