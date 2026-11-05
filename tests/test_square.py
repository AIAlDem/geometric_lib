import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    # area

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_positive_area(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_float_area(self):
        res = area(2.5)
        self.assertEqual(res, 6.25)

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
        self.assertEqual(res, 20)

    def test_float_perimeter(self):
        res = perimeter(2.5)
        self.assertEqual(res, 10.0)

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("5")