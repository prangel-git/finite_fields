import pytest

import congruence

import polynomial

def test_polynomial_mod3():
    mod3 = congruence.Congruence(3)
    poly = polynomial.Polynomial([mod3(1), mod3(1)])
    polycube = poly * poly * poly
    expected_polynomial = polynomial.Polynomial([mod3(1), mod3(0), mod3(0), mod3(1)])

    assert polycube == expected_polynomial
