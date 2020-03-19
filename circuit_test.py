#!/usr/bin/env python3

import unittest

from circuit import *


class TestCircuit(unittest.TestCase):
    def test_domain(self):
        d4 = domain(4)
        self.assertEqual(len(d4), 16)

    def test_sublists(self):
        subs = sublists([1, 2, 3, 4])
        self.assertEqual(len(subs), 16)

    def test_toffoli_generate(self):
        gates = Toffoli.generate(2, 3)
        self.assertEqual(len(gates), 12)

    def test_impact(self):
        not_gate = Toffoli([], 0)
        self.assertEqual(impact(not_gate, 4), 16)


if __name__ == "__main__":
    unittest.main()
