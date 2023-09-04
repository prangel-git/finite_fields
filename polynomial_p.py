from typing import Any


class PolyP:
    def __init__(self, coefficients, characteristic):
        self.coefficients = [a % characteristic for a in coefficients]
        self.characteristic = characteristic


    def __call__(self, x):
        a = self.coefficients
        p = self.characteristic
        output = sum([a_k * x ** k for (a_k, k) in zip(a, range(len(a )))])
        output = output % p
        return output