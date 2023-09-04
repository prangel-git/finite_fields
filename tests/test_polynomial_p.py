import pytest

from polynomial_p import PolyP

from congruence import Congruence

def test_init():
    coefficients = [1, 1]
    characteristic = 3
    poly = PolyP(coefficients, characteristic)
    assert poly.coefficients == coefficients
    assert poly.characteristic == characteristic

def test_eval():
    coefficients = [2, 1]
    characteristic = 3
    poly_p = PolyP(coefficients, characteristic)
    calculated = poly_p(2)
    
    expected = 1

    assert calculated == expected