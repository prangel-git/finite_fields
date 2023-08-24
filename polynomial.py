from itertools import zip_longest

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = [c for c in coefficients]
        erase_leading_zeroes(self.coefficients)
    
    def __call__(self, x):
        evaluation = [self.coefficients[n] * (x ** n) for n in range(len(self.coefficients))]
        return sum(evaluation)
    
    def __add__(self, other):
        result_coefficients = [a_n + b_n for (a_n, b_n) in zip_longest(self.coefficients, other.coefficients, fillvalue=0)]
        return Polynomial(result_coefficients)
    
    def __sub__(self, other):
        result_coefficients = [a_n - b_n for (a_n, b_n) in zip_longest(self.coefficients, other.coefficients, fillvalue=0)]
        return Polynomial(result_coefficients)

    def __mul__(self, other):
        len_a = len(self.coefficients)
        len_b = len(other.coefficients)
        a = self.coefficients
        b = other.coefficients + [0] * len_a
        product_coefficients = [sum([a[k] * b[n-k] for k in range(min(len_a, n+1))]) for n in range(len_a + len_b - 1)]
        return Polynomial(product_coefficients)
    
    def __mod__(self, other):
        
        len_a = len(self.coefficients)
        len_b = len(other.coefficients)
        if len_a < len_b:
            return Polynomial(self.coefficients)
        
        factor_coefficients = [0] * (len_a - len_b + 1)
        factor_coefficients[-1] = self.coefficients[-1] / other.coefficients[-1] 
        factor = Polynomial(factor_coefficients)

        new_polynomial = self - factor * other
        return new_polynomial % other


def erase_leading_zeroes(coefficients):
    while len(coefficients) != 0 and coefficients[-1] == 0:
        coefficients.pop()
    
