import unittest
import rectangle
import square
import triangle
import circle

class RectangleTestCase(unittest.TestCase):
    # Тесты для прямоугольника
    def test_rectangle_area_1(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
    def test_rectangle_area_2(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)
    def test_rectangle_perimeter_1(self):
        res = rectangle.perimeter(10, 4)
        self.assertEqual(res, 28)
    def test_rectangle_perimeter_2(self):
        res = rectangle.perimeter(20, 10)
        self.assertEqual(res, 60)
    # Тесты для квадрата
    def test_square_area_1(self):
        res = square.area(10)
        self.assertEqual(res, 100)
    def test_square_area_2(self):
        res = square.area(0)
        self.assertEqual(res, 0)
    def test_square_perimeter_1(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)
    def test_square_perimeter_2(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
    # Тесты для треугольника
    def test_triangle_area_1(self):
        res = triangle.area(10, 5)
        self.assertEqual(res, 25)
    def test_triangle_area_2(self):
        res = triangle.area(0, 10)
        self.assertEqual(res, 0)
    def test_triangle_perimeter_1(self):
        res = triangle.perimeter(10, 5, 5)
        self.assertEqual(res, 20)
    def test_triangle_perimeter_2(self):
        res = triangle.perimeter(20, 10, 0)
        self.assertEqual(res, 0)
    # Тесты для круга
    def test_circle_area_1(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
    def test_circle_area_2(self):
        res = circle.area(10)
        self.assertEqual(res, 314.1592653589793)
    def test_circle_perimeter_1(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
    def test_circle_perimeter_2(self):
        res = circle.perimeter(20)
        self.assertEqual(res, 125.66370614359172)