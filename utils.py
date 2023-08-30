def gcdExtended(a, b):
 
    # Base Case
    zero = a - a
    one = b // b
    if a == zero:
        return b, zero, one
 
    gcd, x1, y1 = gcdExtended(b % a, a)
 
    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1
 
    return gcd, x, y