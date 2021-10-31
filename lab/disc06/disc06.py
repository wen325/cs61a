class Tree:
    def __init__(self, label, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.label = label
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)

    def is_leaf(self):
        return not self.branches

    def __eq__(self, other):
        return type(other) is type(self) and self.label == other.label \
               and self.branches == other.branches

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def copy_tree(self):
        return Tree(self.label, [b.copy_tree() for b in self.branches])

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    @property
    def second(self):
        return self.rest.first
    
    @second.setter
    def second(self, value):
        self.rest.first = value
        
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
# 1.3

def sum_nums(lnk):
    if lnk == Link.empty:
        return 0
    else:    
        return lnk.first+sum_nums(lnk.rest)    
    
a = Link(1,Link(6,Link(7,Link(8))))   
    
    

# 3.1    
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest
    ()
    """    
    new_list = Link(1)
    n = len(lst_of_lnks)    
    for i in range(n):
        k = 1
        for j in range(n):
            k = k*get_link(lst_of_lnks[j],i)
            
        set_link(new_list,i,k)    
        
    return new_list

def get_link(link,n):
    if link == Link.empty:
        return Link.empty
    elif n == 0:
        return link.first
    else:
        return get_link(link.rest,n-1)

def set_link(link,n,k):                  # tuple is immuttable; when chagne () == Link(9), the origin Link will not chagne
    if n == 0:
        link.first = k
    elif link.rest != Link.empty:            
        return set_link(link.rest, n-1,k)
    else:
        link.rest = Link(k)  

# 3.2    

def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> unique = remove_duplicates(lnk)
    >>> unique
    Link(1, Link(5))
    >> lnk
    Link(1, Link(5))
    """
    
    if lnk.first == lnk.rest.first:
        lnk.first = lnk.rest.first      # both sides do not use [lnk], this will create new object
        lnk.rest = lnk.rest.rest
        return remove_duplicates(lnk)
    else:        
        return lnk

# lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
# unique = remove_duplicates(lnk)

# 4.1
def even_weighted(lst):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [lst[i]*i for i in range(len(lst)) if i%2==0]     

# 4.2

def quicksort_list(lst):
    """
    >>> quicksort_list([3, 1, 4])
    [1, 3, 4]
    """
    if len(lst)<2:
        return lst
    pivot = lst[0]
    less = quicksort_list([i for i in lst if i<pivot])
    greater = quicksort_list([i for i in lst if i>pivot])
    return less + [pivot] + greater

# 4.3

def max_product(lst):
    """Return the maximum product that can be formed using lst
    without using any consecutive numbers
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    n = len(lst)
    if n == 0:
        return 1
    elif n == 1:
        return lst[0]
    else:                         
        return max(max_product(lst[:-1]), lst[n-1]*max_product(lst[:-2]))
        
# 4.4 The tree is ADT tree

def eval_tree(tree):
    """Evaluates an expression tree with functions the root.
    >>> eval_tree(tree(1))
    1
    >>> expr = tree('*', [tree(2), tree(3)])
    >>> eval_tree(expr)
    6
    >>> eval_tree(tree('+', [expr, tree(4), tree(5)]))
    15
    """
    if tree[0] == '+':        
        return sum(eval_tree(b) for b in tree[1:])    
    elif tree[0] == '*':
        return prod(eval_tree(b) for b in tree[1:])
    else:
        return tree[0]
    
def prod(lst):
    k = 1
    for x in lst:
        k = k*x
    return k


# 4.5 the Tree is Class tree

def redundant_map(t, f):
    """
    >>> double = lambda x: x*2
    >>> tree = Tree(1, [Tree(1), Tree(2, [Tree(1, [Tree(1)])])])
    >>> print_levels(redundant_map(tree, double))
    [2] # 1 * 2 ˆ (1) ; Apply double one time
    [4, 8] # 1 * 2 ˆ (2), 2 * 2 ˆ (2) ; Apply double two times
    [16] # 1 * 2 ˆ (2 ˆ 2) ; Apply double four times
    [256] # 1 * 2 ˆ (2 ˆ 3) ; Apply double eight times
    """
    t.label = t.label * f(1)
    new_f = lambda x: f(x)**2
    t.branches = [redundant_map(b, new_f) for b in t.branches]
    return t

double = lambda x: x*2 
tree = Tree(1, [Tree(1), Tree(2, [Tree(1, [Tree(1)])])])

tree = redundant_map(tree,double)

fourth = lambda x: double(x)*2