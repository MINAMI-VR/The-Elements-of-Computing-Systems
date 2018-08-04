from Chapter01 import And
from Chapter01 import Xor
from Chapter01 import Or
from Chapter01 import Mux16
from Chapter01 import Xor16
from Chapter01 import And16
from Chapter01 import Not16
from Chapter01 import Not
from Chapter01 import Or8Way


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


def ALU(x, y, zx, nx, zy, ny, f, no):
    x = Mux16(x, Xor16(x, x), zx)
    x = Mux16(x, Not16(x), nx)
    y = Mux16(y, Xor16(y, y), zy)
    y = Mux16(y, Not16(y), ny)
    z = Mux16(And16(x, y), Add16(x, y), f)
    out = Mux16(z, Not16(z), no)
    zr = Not(Or8Way(out))
    ng = out[len(out) - 1]
    return out, zr, ng
