#!/usr/bin/env python3

N = 3


class Toffoli:
    def __init__(self, inputs, output):
        if output in inputs:
            raise Exception("bad Toffoli gate")
        self.inputs = inputs
        self.output = output

    def __str__(self):
        inputs = ",".join(map(str, self.inputs))
        return f"Toffoli([{inputs}], {self.output})"

    def __call__(self, bits):
        if all(bits[i] for i in self.inputs):
            copy = list(bits)
            copy[self.output] = 1 - copy[self.output]
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


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def signature(circuit, n):
    """
    A representation of all outputs of the circuit.
    """
    outputs = []
    for b in domain(n):
        outputs.append(circuit(b))
    return tuple(outputs)


def sublists(alist):
    if not alist:
        return [[]]
    subsub = sublists(alist[1:])
    return subsub + [[alist[0]] + x for x in subsub]


if __name__ == "__main__":
    print(factorial(8))
