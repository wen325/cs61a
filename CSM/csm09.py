## part 1
# 1
def foo():
    a = 0
    if a < 10:
        print("Hello")
        yield a
        print("World")
        
# 2

def foo_list():
    a = 0
    while a < 10:
        yield a
        a += 1
        
# 3

def hailstone_sequence(n):
    """
    >>> hs_gen = hailstone_sequence(10)
    >>> next(hs_gen)
    10
    >>> next(hs_gen)
    5
    >>> for i in hs_gen:
    print(i)
    16
    8
    4
    2
    1
    """
    while n > 1:
        yield n
        if n%2 == 0:
            n = int(n/2)
        else:
            n = 3*n + 1
    yield n
    
hs_gen = hailstone_sequence(10)

## part 4

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

def all_paths(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(5)]), Tree(3, [Tree(4)])])
    >>> print(list(all_paths(t)))
    [[1, 2, 5], [1, 3, 4]]
    """
    if t.branches == []:
        yield [t.label]
    for branch in t.branches:
        for path in all_paths(branch):
            yield [t.label] + path
            
t = Tree(1, [Tree(2, [Tree(5)]), Tree(3, [Tree(4)])])
print(list(all_paths(t)))
        
            
