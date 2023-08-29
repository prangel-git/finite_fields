import pytest

import utils

def test_extended_euclidean():
    gcd, x, y = utils.gcdExtended(5,3)
    assert gcd == 1
    assert x == -1
    assert y == 2