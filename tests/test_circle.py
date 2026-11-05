import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    # area

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_positive_area(self):
        res = area(5)
        self.assertAlmostEqual(res, math.pi * 5 ** 2)

    def test_float_area(self):
        res = area(2.5)
        self.assertAlmostEqual(res, math.pi * 2.5 ** 2)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area("5")

    # perimeter

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_positive_perimeter(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 2 * math.pi * 5)

    def test_float_perimeter(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 2 * math.pi * 2.5)

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("5")