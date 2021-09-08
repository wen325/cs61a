
add_one = lambda x: x + 1        # adds one to x
square = lambda x: x**2

def compose1(f, g):
    
    return lambda x: f(g(x))

b1 = compose1(add_one,square)


def composite_identity(f, g):

    def diff(x):      
        return compose1(f,g)(x) == compose1(g,f)(x)

    return diff
    # return False

b2 = composite_identity(add_one,square)
