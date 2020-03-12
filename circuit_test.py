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


if __name__ == "__main__":
    unittest.main()
