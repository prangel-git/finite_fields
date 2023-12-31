from utils import gcdExtended


class EquivalenceClass:
    def __init__(self, value, congruence):
        self.congruence = congruence
        self.value = value % self.congruence.mod

    def __add__(self, other):
        return self.congruence(self.value + other.value)
    
    def __sub__(self, other):
        return self.congruence(self.value - other.value)
    
    def __mul__(self, other):
        return self.congruence(self.value * other.value)
    
    def __truediv__(self, other):
        return self * other.inverse()
    
    def __floordiv__(self, other):
        return self * other.inverse()
    
    def __pow__(self, other):
        return self.congruence(self.value ** other)
    
    def inverse(self):
        _, inv, _ = gcdExtended(self.value, self.congruence.mod)
        return self.congruence(inv)
    
    def __eq__(self, other):
        return self.value == other.value and self.congruence == other.congruence
    
    def __repr__(self):
        return f'{self.value} [mod {self.congruence}]'


class Congruence:
    def __init__(self, mod) -> None:
        self.mod = mod

    def __call__(self, value):
        return EquivalenceClass(value, self)
    
    def __repr__(self) -> str:
        return f'{self.mod}'
    
