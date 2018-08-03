import Chapter01 as c1


def HalfAdder(a, b):
    Sum = c1.Xor(a, b)
    carry = c1.And(a, b)
    return Sum, carry


def FullAdder(a, b, c):
    Sum = c1.Or(c1.And(c1.Not(c), c1.Or(c1.And(a, c1.Not(b)), c1.And(c1.Not(a), b))),
                c1.And(c, c1.Or(c1.And(c1.Not(a), c1.Not(b)), c1.And(a, b))))
    carry = c1.And(c1.Or(c, b), a)
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
