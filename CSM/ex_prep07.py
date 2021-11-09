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

    # def __str__(self):
    #     string = '<'
    #     while self.rest is not Link.empty:
    #         string += str(self.first) + ' '
    #         self = self.rest
    #     return string + str(self.first) + '>'
    
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
    
# part 1 #1
def linky_paths(t):
    """
    >>> t = Tree(1, [Tree(2)])
    >>> linky_paths(t)
    >>> t
    Tree(Link(1), [Tree(Link(2, Link(1))]
    """
    def helper(t, path_so_far):
        t.label = Link(t.label, path_so_far)
        print(t.label)
        for branch in t.branches:
            helper(branch, t.label)
            
    helper(t, ())
    
# part 1 #2
    
def find_file_path(t, file_str):
    """
    >>> t = Tree('data', [Tree('comm', [Tree('dummy.py')]),
    Tree('ecc',
    [Tree('hello.py'), Tree('file.py')]), Tree('file2.py')])
    >>> find_file_path(t, 'file2.py')
    '/data/file2.py'
    >>> find_file_path(t, 'dummy.py')
    '/data/comm/dummy.py'
    >>> find_file_path(t, 'hello.py')
    '/data/ecc/hello.py'
    >>> find_file_path(t, 'file.py')
    '/data/ecc/file.py'
    """
    def helper(t, file_str, path_so_far):
        if t.label == file_str:
            return path_so_far + '/' + file_str
        elif t.is_leaf():
            return None
        for branch in t.branches:
            # print(path_so_far + '/' + t.label)
            result = helper(branch, file_str, path_so_far + '/' + t.label)
            if result:
                return result
    return helper(t, file_str, '')

# part 2 #1

def convert_to_string(link):
    """
    >>> link = Link( d a t a , Link( f i l e 2 . p y ))
    >>> convert_to_string(link)
    '/data/file2.py'
    """
    if link.rest is not Link.empty:
        return '/' + link.first + convert_to_string(link.rest)        
    return '/' + link.first


# part 2 #2

def all_paths_linked(t):
    """
    >>> t1 = Tree(1, [Tree(2), Tree(3)])
    >>> t2 = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)])
    ])
    >>> all_paths(t1)
    [Link(1, Link(2)), Link(1, Link(3))]
    >>> all_paths(t2)
    [Link(1, Link(2)), Link(1, Link(3, Link(4))), Link(1,
    Link(3, Link(5)))]
    """
    if t.branches == []:
        return [Link(t.label)]
    result = []
    for branch in t.branches:
        result += [Link(t.label, path) for path in all_paths_linked(branch)]
    return result


# part 2 #3

def find_file_path2(t, file_str):
    """
    >>> t = Tree('data', [Tree('comm', [Tree('dummy.py')]),
    Tree('ecc',
    [Tree('hello.py'), Tree('file.py')]), Tree('file2.py')])
    >>> find_file_path2(t, 'file2.py')
    '/data/file2.py'
    >>> find_file_path2(t, 'dummy.py')
    '/data/comm/dummy.py'
    >>> find_file_path2(t, 'hello.py')
    '/data/ecc/hello.py'
    >>> find_file_path2(t, 'file.py')
    '/data/ecc/file.py'
    """
    for link in all_paths_linked(t):
        original = link
        while link != Link.empty:
            if file_str == link.first:
                return convert_to_string(original)
            link = link.rest

t = Tree('data', [Tree('comm', [Tree('dummy.py')]),Tree('ecc',[Tree('hello.py'), Tree('file.py')]), Tree('file2.py')])
t1 = find_file_path2(t, 'file2.py')

t2 = find_file_path2(t, 'dummy.py')

t3 = find_file_path2(t, 'hello.py')

t4 = find_file_path2(t, 'file.py')

    
# part 2 #4

def skip(lnk, n):
    """
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))
    ))))
    >>> skip(lnk, 2)
    >>> lnk
    Link(1, Link(3, Link(5)))
    >>> lnk2 = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6)
    )))))
    >>> skip(lnk2, 4)
    >>> lnk2
    Link(1, Link(2, Link(3, Link(5, Link(6)))))
    """
    count = 1
    def skipper(lst):
        nonlocal count, n
        count += 1
        if lst == Link.empty:
            return
        elif count == n:
            lst.rest = lst.rest.rest
            count = 1
        return skipper(lst.rest)
    return skipper(lnk)

lnk = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
skip(lnk, 2)

lnk2 = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
skip(lnk2, 4)
