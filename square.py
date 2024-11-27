import unittest
def area(a):
    """Возвращает площадь квадрата"""
    # Параметры:
    #   a (int): длина квадрата
    #   b (int): ширина квадрата  
    # Возвращаемое значение:
    #   a * a: искомая площадь квадрата
    if type(a) is not int:
        raise TypeError("Аргумент должен быть int")
    if a <= 0:
        raise ValueError("Аргумент должен быть больше нуля")
    return a * a

def perimeter(a):
    """Возвращает периметр квадрата"""
    # Параметры:
    #   a (int): длина квадрата
    #   b (int): ширина квадрата
    # Возвращаемое значение:
    #   4 * a: искомый периметр квадрата
    if type(a) is not int:
        raise TypeError("Аргумент должен быть int")
    if a <= 0:
        raise ValueError("Аргумент должен быть больше нуля")
    return 4 * a
class SquareAreaTestCases(unittest.TestCase):
    def test_square_int_first(self):
        self.assertEqual(area(5), 5 * 5)

    def test_square_int_second(self):
        self.assertEqual(area(57285), 57285 * 57285)

    def test_square_string_first(self):
        with self.assertRaises(TypeError):
            area("85")

    def test_square_string_second(self):
        with self.assertRaises(TypeError):
            area("ITMO")

    def test_square_bool_first(self):
        with self.assertRaises(TypeError):
            area(True)

    def test_square_bool_second(self):
        with self.assertRaises(TypeError):
            area(False)

    def test_square_negative_int_first(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_square_negative_int_second(self):
        with self.assertRaises(ValueError):
            area(-59853)

    def test_square_zero_int(self):
        with self.assertRaises(ValueError):
            area(0)
class SquarePerimeterTestCases(unittest.TestCase):
    def test_square_int_first(self):
        self.assertEqual(perimeter(9), 4 * 9)

    def test_square_int_second(self):
        self.assertEqual(perimeter(394732), 4 * 394732)

    def test_square_string_first(self):
        with self.assertRaises(TypeError):
            perimeter("85")

    def test_square_string_second(self):
        with self.assertRaises(TypeError):
            perimeter("ITMO")

    def test_square_bool_first(self):
        with self.assertRaises(TypeError):
            perimeter(True)

    def test_square_bool_second(self):
        with self.assertRaises(TypeError):
            perimeter(False)

    def test_square_negative_int_first(self):
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_square_negative_int_second(self):
        with self.assertRaises(ValueError):
            perimeter(-59853)

    def test_square_zero_int(self):
        with self.assertRaises(ValueError):
            perimeter(0)

if __name__ == '__main__':
    unittest.main()

