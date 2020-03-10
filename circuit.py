#!/usr/bin/env python3


class Toffoli:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"T({self.i}, {self.j}, {self.k})"

    def __call__(self, bits):
        if bits[self.i] and bits[self.j]:
            copy = list(bits)
            copy[self.k] = 1 - copy[self.k]
            return tuple(copy)
        else:
            return bits

    def decomposition(self):
        return [self]


class Composition:
    def __init__(self, circuit1, circuit2):
        self.atoms = circuit1.decomposition() + circuit2.decomposition()

    def __str__(self):
        return "{" + ", ".join(map(str, self.atoms)) + "}"

    def __call__(self, bits):
        accumulator = bits
        for atom in self.atoms:
            accumulator = atom(accumulator)
        return accumulator

    def decomposition(self):
        return self.atoms


def domain(n):
    if n <= 0:
        return [()]

    subdomain = domain(n - 1)
    return [(0,) + x for x in subdomain] + [(1,) + x for x in subdomain]
