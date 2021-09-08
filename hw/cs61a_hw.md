note for cs61a


here is a code example

```python
def no_eleven(n):
    
    if n == 0:
       return [[]]    # it is [[]], not []. Important!
    elif n == 1:
        return [[6],[1]]
    else:
        a, b = no_eleven(n-1), no_eleven(n-2)
    
    return [[6]+s for s in a] + [[1,6] s for s in b]
```
