def wears_jacket(temp,raining):
    return temp < 60 or raining

def handle_overflow(s1,s2):
    if s1 >=30 and s2 >= 30:
        print("No space left in either section")
        
    elif s1 > 30:
        print("Move to Section 2:",30-s2)
    elif s2 > 30:
        print("Move to Section 1:",30-s1)
        
    else:
        print("No over flow")
        
        
def square(x):
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x/0


def is_prime(n):
    y = 2;
    while y <= n-1:
        if n % y == 0:
            return False
        y +=1
    return True
        
def outer(n):
    def inner(m):
        return n-m
    return inner

# def keep_ints(cond,n):
#     if n>1:
#         if cond(n):
#             print(n)
#             return keep_ints(cond,n-1)
#         else:
#             return keep_ints(cond,n-1)

def keep_ints(n):
   def f(cond):
       i = 1
       while i<=n:
            if cond(i):
                print(i)
            i +=1
   return f
     

    
def is_even(x):
    return x % 2 ==0

def test():
    print(test)