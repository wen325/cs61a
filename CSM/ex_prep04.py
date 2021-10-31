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

# 1

def about_equal(t1, t2):
    """Returns whether two trees are 'about equal.'
    Two trees are about equal if and only if they contain
    the same labels the same number of times.
    >> x = tree(1, [tree(2), tree(2), tree(3)])
    >> y = tree(3, [tree(2), tree(1), tree(2)])
    >> about_equal(x, y)
    True
    >> z = tree(3, [tree(2), tree(1), tree(2), tree(3)])
    >> about_equal(x, z)
    False
    """
    def label_counts(t):
        if is_leaf(t):
            return {label(t): 1}
        else:
            counts = dict()
            for b in branches(t) + [[t[0]]]:
                for lab, count in label_counts(b).items():    # not correct
                    if label not in counts:
                        counts[lab] = 0
                    counts[lab] += count
            # print(counts)      
            return counts
    
    return label_counts(t1) == label_counts(t2)

# x = tree(1, [tree(2), tree(2), tree(3)])
# y = tree(3, [tree(2), tree(1), tree(2)])
# about_equal(x, y)

# z = tree(3, [tree(2), tree(1), tree(2), tree(3)])
# about_equal(x, z)


# 1
def decrypt(s, d):
    """List all possible decoded strings of s.
    >>> codes = {
    ... 'alan': 'spooky',
    ... 'al': 'drink',
    ... 'antu': 'your',
    ... 'turing': 'ghosts',
    ... 'tur': 'scary',
    ... 'ing': 'skeletons',
    ... 'ring': 'ovaltine'
    ... }
    >>> decrypt('alanturing', codes)
    ['drink your ovaltine', 'spooky ghosts', 'spooky scary
    skeletons']
    """
    if s == '':
        return []
    ms = []
    if s in d:
        ms.append(d[s])
    for k in range(0,len(s)):
        first, suffix = s[:k], s[k:]
        if first in d:
            for rest in decrypt(suffix,d):     # important
                ms.append(d[first]+' '+rest)
    return ms

codes = {'alan': 'spooky','al': 'drink','antu': 'your','turing': 'ghosts','tur': 'scary','ing': 'skeletons','ring': 'ovaltine'}
decrypt('alanturing', codes)

# 2

def ensure_consistency(fn):
    """Returns a function that calls fn on its argument, returns fn's
    return value, and returns None if fn's return value is different
    from any of its previous return values for those same argument.
    Also returns None if more than 20 calls are made.
    >>> def consistent(x):
    >>> return x
    >>>
    >>> lst = [1, 2, 3]
    >>> def inconsistent(x):
    >>> return x + lst.pop()
    >>>
    >>> a = ensure_consistency(consistent)
    >>> a(5)
    5
    >>> a(5)
    5
    >>> a(6)
    6
    >>> a(6)
    6
    >>> b = ensure_consistency(inconsistent)
    >>> b(5)
    8
    >>> b(5)
    None
    >>> b(6)
    7
    """
    n = 0
    z = {}
    def helper(x):
        nonlocal n,z
        n += 1
        if n > 20:
            return None
        val = fn(x)
        if x not in z:
            z[x] = val
        if z[x] + val > 20:
            return None
        else:
            z[x] = z[x] + val
            return val
    return helper


def consistent(x):
    return x

lst = [1, 2, 3]
def inconsistent(x):
    return x + lst.pop()

a = ensure_consistency(consistent)

b = ensure_consistency(inconsistent)
