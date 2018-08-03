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
    out = [0] * len(a)
    while i < len(a):
        out[i] = Nand(a[i], b[i])
        i = i + 1
    return out


def Not16(x):
    i = 0
    out = [0] * len(x)
    while i < len(x):
        out[i] = Not(x[i])
        i = i + 1
    return out


def And16(a, b):
    i = 0
    out = [0] * len(a)
    while i < len(a):
        out[i] = And(a[i], b[i])
        i = i + 1
    return out


def Mux16(a, b, select):
    i = 0
    out = [0] * len(a)
    while i < len(a):
        out[i] = Mux(a[i], b[i], select)
        i = i + 1
    return out


def Or8Way(x):
    i = 0
    out = 0
    while i < len(x):
        out = Or(out, x[i])
        i = i + 1
    return out


def Mux4Way16(a, b, c, d, select):
    out = Mux16(Mux16(a, b, select[0]), Mux16(c, d, select[0]), select[1])
    return out


def Mux8Way16(a, b, c, d, e, f, g, h, select):
    out = Mux16(Mux4Way16(a, b, c, d, select), Mux4Way16(e, f, g, h, select), select[2])
    return out


def DMux4Way(In, select):
    a = And(In, And(Not(select[0]), Not(select[1])))
    b = And(In, And(select[0], Not(select[1])))
    c = And(In, And(Not(select[0]), select[1]))
    d = And(In, And(select[0], select[1]))
    return a, b, c, d


def DMux8Way(In, select):
    a = And(And(In, Not(select[0])), And(Not(select[1]), Not(select[2])))
    b = And(And(In, select[0]), And(Not(select[1]), Not(select[2])))
    c = And(And(In, Not(select[0])), And(select[1], Not(select[2])))
    d = And(And(In, select[0]), And(select[1], Not(select[2])))
    e = And(And(In, Not(select[0])), And(Not(select[1]), select[2]))
    f = And(And(In, select[0]), And(Not(select[1]), select[2]))
    g = And(And(In, Not(select[0])), And(select[1], select[2]))
    h = And(And(In, select[0]), And(select[1], select[2]))
    return a, b, c, d, e, f, g, h

