# Linked lists

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.second
    3
    >>> s.first = 5
    >>> s.second = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value


    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


def check(link):
    if link is Link.empty:
        print('This linked list is empty!')
        
# 2
def skip(lst):
    """
    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> a
    Link(1, Link(2, Link(3, Link(4))))
    >>> b = skip(a)
    >>> b
    Link(1, Link(3))
    >>> a
    Link(1, Link(2, Link(3, Link(4)))) # Original is unchanged
    """
    
    if lst.rest is Link.empty:
        return Link(lst.first)
    elif lst.rest.rest is Link.empty:
        return Link(lst.first)
    return Link(lst.first,skip(lst.rest.rest))


# 3
def skip_mutate(lst):
    """
    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> b = skip(a)
    >>> b
    None
    >>> a
    Link(1, Link(3))
    """
    if lst.rest is Link.empty:
        return None
    elif lst.rest.rest is Link.empty:
        lst.rest = Link.empty
    lst.rest = skip(lst.rest.rest)    
    
# 4

def reverse(lst):
    """
    >>> a = Link(1, Link(2, Link(3)))
    >>> b = reverse(a)
    >>> b
    Link(3, Link(2, Link(1)))
    >>> a
    Link(1, Link(2,Link(3)))    
    """
    b = Link.empty
    
    while lst is not Link.empty:
        b = Link(lst.first,b)
        lst = lst.rest
    return b
        
        
        
        
        
    # if b.rest.rest is Link.empty:
    #     b.first, b.rest.first = b.rest.first, b.first
            
    # else:
    #     b.first, b.rest.first = b.rest.first, b.first
    #     b.rest = reverse(b.rest)
    #     b.first, b.rest.first = b.rest.first, b.first
    
    # return b



# Midterm Review

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
    
# 1

def contains_n(elem, n, t):
    """
    >>> t1 = Tree(1, [Tree(1, [Tree(2)])])
    >>> contains_n(1, 2, t1)
    True
    >>> contains_n(2, 2, t1)
    False
    >>> contains_n(2, 1, t1)
    True
    >>> t2 = Tree(1, [Tree(2), Tree(1, [Tree(1), Tree(2)])])
    >>> contains_n(1, 3, t2)
    True
    >>> contains_n(2, 2, t2) # Not on a path
    False
    """
    if n == 0:
        return True
    elif t.is_leaf():
        return n == 1 and t.label == elem
    elif t.label == elem:
        return True in [contains_n(elem, n-1, b) for b in t.branches]
    else:
        return True in [contains_n(elem, n, b) for b in t.branches]
    
    
# 2

def factor_tree(n):
    for i in range(2,n):
        if n % i == 0:
            return Tree(n, [Tree(i),factor_tree(int(n/i))])
                        
    return Tree(n)