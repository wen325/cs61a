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
    
    
def append(link, value):
    """Mutates link by adding value to the end of link."""
    if link.rest is Link.empty:
        link.rest = Link(value)
    else:
        append(link.rest, value)
        
def extend(link1, link2):
    """Mutates link1 so that all elements of link2 are added
    to the end of link1.
    """
    while link2 is not Link.empty:
        append(link1, link2.first)
        link2 = link2.rest
        
def conserve_links(a, b):    # not understand question
    """Makes Linked List a share as many Link instances as possible with
    Linked List b.a can use b's i-th Link instance as its i-th Link
    instance if a and b have the same element at position i.
    Should mutate a. b is allowed to be destroyed. Returns the new first
    Link instance of a.
    >>> x = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    >>> y = Link(1, Link(9, Link(3, Link(4, Link(9, Link(6))))))
    >>> z = conserve_links(x, y)
    >>> curr_x, curr_z = x, z
    >>> while curr_z is not Link.empty:
    >>> assert curr_z.first == curr_x.first
    >>> curr_x, curr_z = curr_x.rest, curr_z.rest
    >>> assert z == y
    >>> assert z.rest.rest == y.rest.rest
    >>> assert z.rest.rest.rest.rest.rest == y.rest.rest.rest.rest.rest
    >>> assert z.rest.rest.rest.rest.rest == y.rest.rest.rest.rest.rest
    """
    if a.first == b.first:
        b.rest = conserve_links(a.rest,b.rest)
        return b
    else:
        return a

def slice_reverse(s, i, j):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> slice_reverse(s, 1, 2)
    >>> s
    Link(1, Link(2, Link(3)))
    >>> s = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> slice_reverse(s, 2, 4)
    >>> s
    Link(1, Link(2, Link(4, Link(3, Link(5)))))
    """
    start = s
    for _ in range(i-1):
        start = start.rest
        
    reverse = Link.empty    
    current = start
    if j-i > 1:
        for _ in range(j-i):
            reverse = Link(current.first,reverse)
            current = current.rest        
        while current is not Link.empty:
              append(reverse,current.first)
              current = current.rest
        s.rest = reverse
