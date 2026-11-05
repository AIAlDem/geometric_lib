import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    # area

    def test_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_zero_side_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_positive_area(self):
        res = area(5, 10)
        self.assertEqual(res, 50)

    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_float_area(self):
        res = area(2.5, 3.5)
        self.assertEqual(res, 8.75)

    def test_negative_first_side_area(self):
        with self.assertRaises(ValueError):
            area(-5, 10)

    def test_negative_second_side_area(self):
        with self.assertRaises(ValueError):
            area(5, -10)

    def test_two_negative_sides_area(self):
        with self.assertRaises(ValueError):
            area(-5, -10)

    def test_string_first_side_area(self):
        with self.assertRaises(TypeError):
            area("3", 10)

    def test_string_second_side_area(self):
        with self.assertRaises(TypeError):
            area(3, "10")

    # perimeter

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_zero_side_perimeter(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_positive_perimeter(self):
        res = perimeter(5, 10)
        self.assertEqual(res, 30)

    def test_square_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_float_perimeter(self):
        res = perimeter(2.5, 3.5)
        self.assertEqual(res, 12.0)

    def test_negative_first_side_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 10)

    def test_negative_second_side_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(5, -10)

    def test_two_negative_sides_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-5, -10)

    def test_string_first_side_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("3", 10)

    def test_string_second_side_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter(3, "10")