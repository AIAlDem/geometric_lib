import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    # area

    def test_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_zero_side_area(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_zero_height_area(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_positive_area(self):
        res = area(5, 4)
        self.assertEqual(res, 10)

    def test_float_area(self):
        res = area(2.5, 3.5)
        self.assertEqual(res, 4.375)

    def test_negative_side_area(self):
        with self.assertRaises(ValueError):
            area(-5, 4)

    def test_negative_height_area(self):
        with self.assertRaises(ValueError):
            area(5, -4)

    def test_two_negative_area(self):
        with self.assertRaises(ValueError):
            area(-5, -4)

    def test_string_side_area(self):
        with self.assertRaises(TypeError):
            area("5", 4)

    def test_string_height_area(self):
        with self.assertRaises(TypeError):
            area(5, "4")

    # perimeter

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_zero_side_perimeter(self):
        res = perimeter(0, 4, 5)
        self.assertEqual(res, 9)

    def test_positive_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_float_perimeter(self):
        res = perimeter(2.5, 3.5, 4.5)
        self.assertEqual(res, 10.5)

    def test_negative_side_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)

    def test_two_negative_sides_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-3, -4, 5)

    def test_string_side_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("3", 4, 5)