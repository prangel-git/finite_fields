import pytest

from finite_field import gf

def test_init():
    gf7 = gf(7)
    assert gf7.characteristic == 7
    assert gf7.dimension == 1

