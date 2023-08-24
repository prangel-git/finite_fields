import pytest

import polynomial

def test_polynomial_construction():
    poly = polynomial.Polynomial(range(2))
    assert poly.coefficients == [0, 1]

def test_evaluate_polynomial():
    coeffients = [1, 2]
    poly = polynomial.Polynomial(coeffients)
    assert poly(2) == 5

def test_add_polynomials():
    poly1 = polynomial.Polynomial([1,2,3])
    poly2 = polynomial.Polynomial([0,1,2,1])
    addition = poly1 + poly2
    assert addition.coefficients == [1, 3, 5, 1]