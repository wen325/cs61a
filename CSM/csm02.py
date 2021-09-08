# q 4
def list_of_lists(lst):
    """
    >>> list_of_lists([1, 2, 3])
    [[0], [0, 1], [0, 1, 2]]
    >>> list_of_lists([1])
    [[0]]
    >>> list_of_lists([])
    []
    """
    new_list = []
    for i in range(len(lst)):
        new_list += [[0]+lst[0:i]]
            
    return new_list


# Tree

def tree(label,branches=[]):
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:] #returns a list of branches


#q 1

e_tree = tree(4,
            [tree(5, []),
                tree(2,
                    [tree(2, []),
                    tree(1, [])]),
             tree(1, []),
             tree(8,
                [tree(4, [])])])


t = tree(9,
         [tree(2),
          tree(4,
               [tree(1)]),
          tree(4,
               [tree(7),
                tree(3)])
          ])

#q 2
label(t)
branches(t)[2]
branches(branches(t)[2])[0]

#q 3
def find_tree(t,n):
    if label(t) == n:
        return True
    else:
        for b in branches(t):
            if find_tree(b,n):
                return True
    return False

#q 4

def sum_of_nodes(t):
    sum = label(t)
    if len(t)<2:
        return t[0]
    else:
        for b in branches(t):
            sum += sum_of_nodes(b)
    return sum
