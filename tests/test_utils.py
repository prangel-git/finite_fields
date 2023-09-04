import pytest

import utils

def test_extended_euclidean():
    gcd, x, y = utils.gcdExtended(5,3)
    assert gcd == 1
    assert x == -1
    assert y == 2

def test_is_prime():
    assert utils.is_prime(2)
    assert not utils.is_prime(4)