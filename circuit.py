#!/usr/bin/env python3

N = 3


class Toffoli:
    def __init__(self, inputs, output):
        if output in inputs:
            raise Exception("bad Toffoli gate")
        self.inputs = tuple(inputs)
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

    @staticmethod
    def generate(fanin, n):
        """
        All Toffoli gates over n bits, with at most fanin inputs.
        """
        answer = []
        for i in range(n):
            others = [x for x in range(n) if x != i]
            for sublist in sublists(others):
                if len(sublist) > fanin:
                    continue
                answer.append(Toffoli(sublist, i))
        return answer

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
    """
    All sublists of the given list.
    """
    if not alist:
        return [[]]
    subsub = sublists(alist[1:])
    return subsub + [[alist[0]] + x for x in subsub]


# TODO: test this
def reachable(fanin, n):
    """
    Figure out what circuits are reachable from gates with limited fanin.
    """
    seen = set()
    answer = []
    atoms = Toffoli.generate(fanin, n)
    pending = list(atoms)
    while pending:
        circuit = pending.pop()
        sig = signature(circuit, n)
        if sig in seen:
            continue
        seen.add(sig)
        if len(seen) % 10000 == 0:
            print(f"found {len(seen)} unique circuits")
        answer.append(circuit)
        more = [Composition(circuit, g) for g in atoms]
        pending = more + pending
    return answer


if __name__ == "__main__":
    n = 4
    fanin = 1
    r = reachable(fanin, n)
    for c in r:
        sig = signature(c, n)
        print(sig)
    print(len(r))
