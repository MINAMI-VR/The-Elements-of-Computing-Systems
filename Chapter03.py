from Chapter01 import Mux
from Chapter01 import Mux16
from Chapter02 import Inc16


class DFF:
    q0 = 0
    q1 = 0

    def dff(self, In):
        self.q1 = self.q0
        self.q0 = In
        out = self.q1
        return out


class Bit:
    q = 0

    def bit(self, In, load):
        self.q = Mux(self.q, In, load)
        return self.q


class Register:
    q = [0] * 16

    def register(self, In, load):
        self.q = Mux16(self.q, In, load)
        return self.q


class RAM8:
    q = [[0] * 16] * 8

    def ram8(self, In, address, load):
        p = address[0] + 2 * address[1] + 4 * address[2]
        self.q[p] = Mux16(self.q[p], In, load)
        return self.q[p]


class RAM64:
    q = [[0] * 16] * 64

    def ram64(self, In, address, load):
        p = 0
        i = 0
        while i < 6:
            p = p + address[i] * pow(2, i)
            i = i + 1
        self.q[p] = Mux16(self.q[p], In, load)
        return self.q[p]


class RAM16K:
    q = [[0] * 16] * 16384

    def ram16k(self, In, address, load):
        p = 0
        i = 0
        while i < 14:
            p = p + address[i] * pow(2, i)
            i = i + 1
        self.q[p] = Mux16(self.q[p], In, load)
        return self.q[p]


class PC:
    q = [0] * 16
    q0 = [0] * 16

    def pc(self, In, inc, load, reset):
        q_inc = Inc16(self.q)
        self.q = Mux16(self.q, q_inc, inc)
        self.q = Mux16(self.q, In, load)
        self.q = Mux16(self.q, self.q0, reset)
        return self.q


r = PC()
while 1:
    a = [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0]
    b = [1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0]
    c = [1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0]
    d = [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0]
    e = [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0]
    f = [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0]
    g = [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0]
    h = [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1]
    arr = [a, b, c, d, e, f, g, h]
    print(r.pc(a, int(input("inc")), int(input("load")), int(input("reset"))))
