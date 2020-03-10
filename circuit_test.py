#!/usr/bin/env python3

import unittest

from circuit import *


class TestCircuit(unittest.TestCase):
    def test_domain(self):
        d4 = domain(4)
        self.assertEqual(len(d4), 16)


if __name__ == "__main__":
    unittest.main()
