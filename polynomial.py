from itertools import zip_longest

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = [c for c in coefficients]
        self.degree = len(coefficients)
    
    def __call__(self, x):
        evaluation = [self.coefficients[n] * (x ** n) for n in range(self.degree)]
        return sum(evaluation)
    
    def __add__(self, other):
        result_coefficients = [a_n + b_n for (a_n, b_n) in zip_longest(self.coefficients, other.coefficients, fillvalue=0)]
        return Polynomial(result_coefficients)


    

