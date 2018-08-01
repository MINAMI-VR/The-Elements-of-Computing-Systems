def Nand(a, b):
    if a + b == 2:
        out = 0
    else:
        out = 1
    return out


def Not(x):
    out = Nand(x, x)
    return out


def And(a, b):
    out = Not(Nand(a, b))
    return out


def Or(a, b):
    out = Nand(Not(a), Not(b))
    return out


def Xor(a, b):
    out = And(Nand(a, b), Or(a, b))
    return out


def Mux(a, b, select):
    out = Or(And(a, Not(select)), And(b, select))
    return out


def DMux(In, select):
    a = And(In, Not(select))
    b = And(In, select)
    return a, b


def Nand16(a, b):
    i = 0
    out = [0] * 16
    while i < 16:
        out[i] = Nand(a[i], b[i])
        i = i + 1
    return out


def Not16(x):
    i = 0
    out = [0] * 16
    while i < 16:
        out[i] = Not(x[i])
        i = i + 1
    return out


def And16(a, b):
    i = 0
    out = [0] * 16
    while i < 16:
        out[i] = And(a[i], b[i])
        i = i + 1
    return out


def Mux16(a, b, select):
    i = 0
    out = [0] * 16
    while i < 16:
        out[i] = Mux(a[i], b[i], select)
        i = i + 1
    return out


def Or8Way(x):
    i = 0
    out = 0
    while i < 16:
        out = Nand(out, x[i])
        i = i + 1
    return out
