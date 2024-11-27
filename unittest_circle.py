import unittest
import math
from src.circle import area, perimeter

class CircleAreaTestCases(unittest.TestCase):

    def test_circle_int_positive(self):
        self.assertEqual(area(5), math.pi × 5 × 5)
        self.assertEqual(area(57285), math.pi × 57285 × 57285)

    def test_circle_string(self):
        with self.assertRaises(TypeError):
            area("85")
        with self.assertRaises(TypeError):
            area("ITMO")

    def test_circle_bool(self):
        with self.assertRaises(TypeError):
            area(True)
        with self.assertRaises(TypeError):
            area(False)

    def test_circle_negative(self):
        with self.assertRaises(ValueError):
            area(-5)
        with self.assertRaises(ValueError):
            area(-59853)

    def test_circle_zero(self):
        with self.assertRaises(ValueError):
            area(0)
class CirclePerimeterTestCases(unittest.TestCase):

    def test_circle_int_positive(self):
        self.assertEqual(perimeter(7), 2 * math.pi * 7)
        self.assertEqual(perimeter(57285), 2 * math.pi * 57285)

    def test_circle_string(self):
        with self.assertRaises(TypeError):
            perimeter("85")
        with self.assertRaises(TypeError):
            perimeter("ITMO")

    def test_circle_bool(self):
        with self.assertRaises(TypeError):
            perimeter(True)
        with self.assertRaises(TypeError):
            perimeter(False)

    def test_circle_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-5)
        with self.assertRaises(ValueError):
            perimeter(-59853)

    def test_circle_zero(self):
        with self.assertRaises(ValueError):
            perimeter(0)

if __name__ == '__main__':
    unittest.main()
