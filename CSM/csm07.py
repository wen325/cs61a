a = 2
def foo():
    a = 10
    return lambda x: x + a
bar = foo()
bar(10)