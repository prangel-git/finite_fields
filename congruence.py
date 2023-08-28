
class EquivalenceClass:
    def __init__(self, value, congruence):
        self.congruence = congruence
        self.value = value % self.congruence.mod

    def __add__(self, other):
        if other == 0:
            return self.congruence(self.value) 
        return self.congruence(self.value + other.value)
    
    def __sub__(self, other):
        if other == 0:
            return self.congruence(self.value)
        return self.congruence(self.value - other.value)
    
    def __mul__(self, other):
        if other == 1:
            return self.congruence(self.value)
        return self.congruence(self.value * other.value)
    
    def __truediv__(self, other):
        return self * other.inverse()
    
    def inverse(self):
        _, inv, _ = gcdExtended(self.value, self.congruence.mod)
        return self.congruence(inv)


class Congruence:
    def __init__(self, mod) -> None:
        self.mod = mod

    def __call__(self, value):
        return EquivalenceClass(value, self)
    

def gcdExtended(a, b):
 
    # Base Case
    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = gcdExtended(b % a, a)
 
    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1
 
    return gcd, x, y
