# nonlocal
# q 1.1
def stepper(num):
    def step():
        nonlocal num
        num +=1
        return num
    return step

# q 1.2

lamb = 'da'
def da(da):
    def lamb(lamb):
        nonlocal da
        def da(nk):
            da = nk + ['da']
            da.append(nk[0:2])
            return nk.pop()
    da(lamb)
    return da([[1],2])+3

# q 1.3

def memory(n):
    x = n;
    def new_fn(fn):
        nonlocal x
        x = fn(x)      
        print(x)
        return new_fn        
    return new_fn

# q 2.1

# q 2.2

def add_this_many(x,el,lst):
    count = 0
    for i in lst:
        if x == i:
            count +=1
    for i in range(count):
        lst.append(el)
            
    return lst

def reverse(lst):
    if len(lst)<2:
        return lst
    return reverse(lst[1:])+[lst[0]]

# q 3.2

def group_by(s,fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    """
    dic = {}
    for i in s:
        if fn(i) in dic:
            dic[fn(i)].append(i)
        else:    
            dic[fn(i)] = [i]
    return dic

# q 3.3
    
def replace_all_deep(d,x,y):
    """
    >>> d = {1: {2: 'x', 'x': 4}, 2: {4: 4, 5: 'x'}}
    >>> replace_all_deep(d, 'x', 'y')
    >>> d
    {1: {2: 'y', 'x': 4}, 2: {4: 4, 5: 'y'}}
    """
    for key in d:        
        if type(d[key]) == dict:
            replace_all_deep(d[key],x,y)        
        elif d[key] == x:
            d[key] = y
            
    return d
    # for value in d.values():        
    #     if type(value) == dict:
    #         value = replace_all_deep(value,x,y)        
    #     elif value == x:
    #         value = y
    # return d
    
    
