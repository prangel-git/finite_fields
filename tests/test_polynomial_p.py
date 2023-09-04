import pytest

from polynomial_p import PolyP

import polynomial

def test_init():
    coefficients = [1, 1]
    characteristic = 3
    poly = PolyP(coefficients, characteristic)
    assert poly.coefficients == coefficients
    assert poly.characteristic == characteristic