import pytest

import congruence

def test_construction_congruence():
    mod3 = congruence.Congruence(3)
    five_mod3 = mod3(5)

    assert five_mod3.value == 2

def test_addition_congruence():
    mod3 = congruence.Congruence(3)
    five = mod3(5)
    seven = mod3(7)

    addition = five + seven
    expected = mod3(0)

    assert addition.value == expected.value

def test_subtraction_congruence():
    mod3 = congruence.Congruence(3)
    five = mod3(5)
    seven = mod3(7)

    addition = five - seven
    expected = mod3(-2)

    assert addition.value == expected.value


def test_product_congruence():
    mod3 = congruence.Congruence(3)
    five = mod3(5)
    seven = mod3(7)

    addition = five * seven
    expected = mod3(35)

    assert addition.value == expected.value

def test_division_congruence():
    mod3 = congruence.Congruence(3)
    one = mod3(1)
    two = mod3(2)

    addition = one / two
    expected = mod3(2)

    assert addition.value == expected.value

def test_eq():
    mod3 = congruence.Congruence(3)
    assert mod3(1) == mod3(4)

def test_repr():
    mod3 = congruence.Congruence(3)
    assert repr(mod3(4)) == '1 [mod 3]'

