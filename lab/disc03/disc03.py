# Constructor
import typing


def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label]+list(branches)

# Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return(tree[1:])

# For convenience
def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree)!=list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


t = tree(1,[tree(3,[tree(4),tree(5),tree(6)]),tree(2)])

# q 3.1

def tree_max(t):
    """Return the max of a tree."""  
    if is_leaf(t):
        return label(t)
    else:
        return max([label(t)]+[tree_max(branch) for branch in branches(t)])
    
# q 3.2

def height(t):
    """Return the height of a tree"""
    if is_leaf(t):
        return 0
    else:
        return 1+max([height(branch) for branch in branches(t)])

# q 3.3

def square_tree(t):
    """Return a tree with the square of every element in t"""        
    return [label(t)**2]+[square_tree(b) for b in branches(t)]
        
# q 3.4     
        
def find_path(tree,x):
    if x==label(tree):
        return [x]
    for b in branches(tree):
        path = find_path(tree,x)
        if path:
            return [label(tree)] + path
        
# q 3.5

def prune(t,k):
    if k==0:
        return [label(t)]
    return [label(t)] + [prune(b,k-1) for b in branches(t)]    

               