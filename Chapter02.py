from Chapter01 import And
from Chapter01 import Xor
from Chapter01 import Or

def HalfAdder(a, b):
    Sum = Xor(a, b)
    carry = And(a, b)
    return Sum, carry


def FullAdder(a, b, c):
    Sum1, carry1 = HalfAdder(a, b)
    Sum, carry2 = HalfAdder(Sum1, c)
    carry = Or(carry1, carry2)
    return Sum, carry


def Add16(a, b):
    c = 0
    i = 0
    out = [0] * len(a)
    while i < len(a):
        out[i], c = FullAdder(a[i], b[i], c)
        i = i + 1
    return out


def Inc16(In):
    inc = [0] * len(In)
    inc[0] = 1
    out = Add16(In, inc)
    return out
