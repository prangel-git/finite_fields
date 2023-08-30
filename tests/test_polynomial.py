import pytest

from polynomial import Polynomial
from polynomial import find_largest_factor

def test_construction():
    poly = Polynomial(range(2))
    assert poly.coefficients == [0, 1]

def test_leading_zeroes():
    poly = Polynomial([1, 2, 0])
    assert poly == Polynomial([1, 2])


def test_evaluate():
    coeffients = [1, 2]
    poly = Polynomial(coeffients)
    assert poly(2) == 5

def test_add():
    poly1 = Polynomial([1,2,3])
    poly2 = Polynomial([0,1,2,1])
    addition = poly1 + poly2
    assert addition == Polynomial([1, 3, 5, 1])

def test_subtraction():
    poly1 = Polynomial([1,2,3,1])
    poly2 = Polynomial([0,1,2,1])
    addition = poly1 - poly2
    assert addition == Polynomial([1, 1, 1])
    

def test_multiplication():
    poly1 = Polynomial([1,2,1])
    poly2 = Polynomial([0,1,1])
    addition = poly1 * poly2
    assert addition == Polynomial([0, 1, 3, 3, 1])

def test_multiplication_2():
    poly1 = Polynomial([0,1])
    poly2 = Polynomial([1,1])
    addition = poly1 * poly2
    assert addition == Polynomial([0, 1, 1])

def test_mod():
    poly1 = Polynomial([1,2,1])
    poly2 = Polynomial([1,1])
    mod = poly1 % poly2
    assert mod == Polynomial([])

def test_eq():
    p = Polynomial([1,2,3])
    q = Polynomial([1,2,3])

    assert p == q 

def test_floordiv():
    p = Polynomial([1,0,2,3]) 
    q = Polynomial([1,0,2]) 
    r = Polynomial([1, 2])

    assert (p*q + r) // q == p

def test_find_largest_factor():
    p = Polynomial([1,0,2,4]) 
    q = Polynomial([1,0,2])

    expected = Polynomial([0, 2])
    calculated = find_largest_factor(p, q)

    assert calculated == expected

def test_polynomial_repr():
    p = Polynomial([])
    assert repr(p) == '0'
    
    

