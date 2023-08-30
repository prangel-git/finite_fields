from itertools import zip_longest

from utils import gcdExtended

class Polynomial:
    def __init__(self, coefficients, indeterminate = 'x'):
        self.coefficients = [c for c in coefficients]
        self.indeterminate = indeterminate
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
        a = self.coefficients
        b = other.coefficients
        len_a = len(a)
        len_b = len(b)
        len_c = len_a + len_b - 1

        c = [0] * len_c
        for n in range(len_c):
            sum_from = max(0, n - len_b + 1)
            sum_to = min(len_a, n + 1)
            if sum_from < sum_to:
                c[n] = a[sum_from] * b[n-sum_from]
                for k in range(sum_from + 1, sum_to):
                    c[n] += a[k] * b[n-k]
        
        return Polynomial(c)

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
    
    def __eq__(self, other):
        return self.coefficients == other.coefficients
    
    def __floordiv__(self, other):
        if other.is_zero():
            raise ZeroDivisionError
        elif self.degree() < other.degree():
            return Polynomial([])

        factor = find_largest_factor(self, other)
        return factor + ((self - (other * factor)) // other)
    
    def __repr__(self):
        if self.is_zero():
            return '0'
        
        is_first_non_zero_coefficient = True
        polynomial_string = ''
        indeterminate = self.indeterminate
        for i in range(len(self.coefficients)):
            if not self.is_zero_coefficient(i):
                if self.is_one_coefficient(i):
                    if i == 0:
                        polynomial_string = '1 +' + polynomial_string
                    elif i == 1:
                        polynomial_string = f'{indeterminate} + ' + polynomial_string
                    else:
                        polynomial_string = f'{indeterminate} ** {i} + ' + polynomial_string
                else:
                    if i == 1:
                        polynomial_string = f'{self.coefficients[i]} x + ' + polynomial_string
                    else:
                        polynomial_string = f'{self.coefficients[i]} {indeterminate} ** {i} + ' + polynomial_string
                
                if is_first_non_zero_coefficient:
                    is_first_non_zero_coefficient = False
                    polynomial_string = polynomial_string[:-3]


        return polynomial_string 

    def is_zero_coefficient(self, k):
        return self.coefficients[k] == self.coefficients[k] - self.coefficients[k]

    def is_one_coefficient(self, k):
        return self.coefficients[k] == self.coefficients[k] // self.coefficients[k]
    
    def is_zero(self):
        return self.coefficients == []
    
    def degree(self):
        return len(self.coefficients) - 1
    



def erase_leading_zeroes(coefficients):
    while len(coefficients) != 0 and coefficients[-1] == coefficients[-1]-coefficients[-1]:
        coefficients.pop()

def find_largest_factor(a, b):
    lead_coefficient_a = a.coefficients[-1]
    lead_coefficient_b = b.coefficients[-1]
    zero = lead_coefficient_a - lead_coefficient_a
    answer = [zero] * (a.degree() - b.degree() + 1)
    answer[-1] = lead_coefficient_a / lead_coefficient_b 
    return Polynomial(answer)