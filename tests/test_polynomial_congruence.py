import pytest

import congruence

import polynomial

'''
def test_polynomial_mod3():
    mod3 = congruence.Congruence(3)
    poly = polynomial.Polynomial([mod3(1), mod3(1)])
    polycube = poly * poly * poly

    assert polycube.coefficients == [mod3(1), 0, 0, mod3(1)]
'''    

def test_product_with_contant():
    mod3 = congruence.Congruence(3)
    five = mod3(5)
    calculated = five + 0
    assert calculated.value == 2
