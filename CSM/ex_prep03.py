# constructor

def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch)
    
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree)!=list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

# q1
def sum_range(t):
    """Returns the range of the sums of t, that is, the
    difference between the largest and the smallest
    sums of t."""
    def helper(t):
        if is_leaf(t):            
            return [label(t),label(t)]
        else:
            a = min([helper(b)[1] for b in branches(t)])
            b = max([helper(b)[0] for b in branches(t)])
            x = label(t)
            return [b + x, a + x]
    x, y = helper(t)
    return x - y

def sum_tree(t):
    sum = 0
    sum_list=[]
    def helper(t,sum):
        if is_leaf(t):                
            return sum_list.append(sum + label(t))
        else:
            sum += label(t)
            [helper(b,sum) for b in branches(t)]
    helper(t,sum)    
    return max(sum_list)-min(sum_list)

# q2

def no_eleven(n):
    
    if n == 0:
       return [[]]
    elif n == 1:
        return [[6],[1]]
    else:
        a, b = no_eleven(n-1), no_eleven(n-2)
    
    return [[6]+s for s in a] + [[1,6]+s for s in b]

# q3

def eval_with_add(t):
    """Evaluate an expression tree of * and + using only
    addition.
    >>> plus = Tree('+', [Tree(2), Tree(3)])
    >>> eval_with_add(plus)
    5
    >>> times = Tree('*', [Tree(2), Tree(3)])
    >>> eval_with_add(times)
    6
    >>> deep = Tree('*', [Tree(2), plus, times])
    >>> eval_with_add(deep)
    60
    >>> eval_with_add(Tree('*'))
    1
    """
    if label(t) == '+':
        return sum(eval_with_add(b) for b in branches(t))
    elif label(t) == '*':
        total = 1
        for b in branches(t):
            total, term = 0, total
            for i in range(eval_with_add(b)):
                total = total + term
        return total
    else:
        return label(t)

            
plus = tree('+', [tree(2), tree(3)])
plus_2 = tree('+', [tree(2), tree(3),tree(4)])

times = tree('*', [tree(2), tree(3)])

deep = tree('*', [tree(2), plus, times])

# t = tree(5,[tree(1,[tree(7,[tree(4,[tree(3)])]),tree(2)]),tree(2,[tree(0),tree(9)])])
