import pytest

import polynomial

def test_construction():
    poly = polynomial.Polynomial(range(2))
    assert poly.coefficients == [0, 1]

def test_leading_zeroes():
    poly = polynomial.Polynomial([1, 2, 0])
    assert poly.coefficients == [1, 2]


def test_evaluate():
    coeffients = [1, 2]
    poly = polynomial.Polynomial(coeffients)
    assert poly(2) == 5

def test_add():
    poly1 = polynomial.Polynomial([1,2,3])
    poly2 = polynomial.Polynomial([0,1,2,1])
    addition = poly1 + poly2
    assert addition.coefficients == [1, 3, 5, 1]

def test_subtraction():
    poly1 = polynomial.Polynomial([1,2,3,1])
    poly2 = polynomial.Polynomial([0,1,2,1])
    addition = poly1 - poly2
    assert addition.coefficients == [1, 1, 1]
    

def test_multiplication():
    poly1 = polynomial.Polynomial([1,2,1])
    poly2 = polynomial.Polynomial([0,1,1])
    addition = poly1 * poly2
    assert addition.coefficients == [0, 1, 3, 3, 1]

def test_multiplication_2():
    poly1 = polynomial.Polynomial([0,1])
    poly2 = polynomial.Polynomial([1,1])
    addition = poly1 * poly2
    assert addition.coefficients == [0, 1, 1]

def test_mod():
    poly1 = polynomial.Polynomial([1,2,1])
    poly2 = polynomial.Polynomial([1,1])
    mod = poly1 % poly2
    assert mod.coefficients == []


