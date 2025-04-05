"""Docstring."""

import unittest
from tasks.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Docstring."""

    def setUp(self):
        self.calculator = Calculator()

    def test_sum(self):
        self.assertEqual(self.calculator.sum(2, 3), 5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(7, 3), 4)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 3), 2)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(16), 4)

    def test_pi(self):
        self.assertEqual(self.calculator.pi(0), 0)


if __name__ == "__main__":
    unittest.main()
