from math_lib import MyMath
from math_lib import ZeroDivisionError
import unittest


class MyMathTests(unittest.TestCase):

    def setUp(self):
        self.MyMath = MyMath()

    def tearDown(self):
        del self.MyMath

    # tests for addition
    def test_addition_positive_positive(self):
        self.assertEqual(9, self.MyMath.addition_two_numbers(2, 7))

    def test_addition_positive_zero(self):
        self.assertEqual(2, self.MyMath.addition_two_numbers(2, 0))

    def test_addition_zero_positive(self):
        self.assertEqual(2, self.MyMath.addition_two_numbers(0, 2))

    def test_addition_positive_negative(self):
        self.assertEqual(-6, self.MyMath.addition_two_numbers(1, -7))

    def test_addition_negative_positive(self):
        self.assertEqual(-6, self.MyMath.addition_two_numbers(-7, 1))

    def test_addition_negative_negative(self):
        self.assertEqual(-3, self.MyMath.addition_two_numbers(-2, -1))

    def test_addition_negative_zero(self):
        self.assertEqual(9, self.MyMath.addition_two_numbers(9, 0))

    def test_addition_zero_negative(self):
        self.assertEqual(9, self.MyMath.addition_two_numbers(0, 9))

    def test_addition_zero_zero(self):
        self.assertEqual(0, self.MyMath.addition_two_numbers(0, 0))

    # tests for subtraction
    def test_subtraction_positive_positive(self):
        self.assertEqual(7, self.MyMath.subtraction_two_numbers(9, 2))

    def test_subtraction_positive_negative(self):
        self.assertEqual(4, self.MyMath.subtraction_two_numbers(3, -1))

    def test_subtraction_negative_positive(self):
        self.assertEqual(-6, self.MyMath.subtraction_two_numbers(-4, 2))

    def test_subtraction_zero_positive(self):
        self.assertEqual(-4, self.MyMath.subtraction_two_numbers(0, 4))

    def test_subtraction_positive_zero(self):
        self.assertEqual(4, self.MyMath.subtraction_two_numbers(4, 0))

    def test_subtraction_negative_negative(self):
        self.assertEqual(-7, self.MyMath.subtraction_two_numbers(-9, -2))

    def test_subtraction_negative_zero(self):
        self.assertEqual(-5, self.MyMath.subtraction_two_numbers(-5, 0))

    def test_subtraction_zero_negative(self):
        self.assertEqual(5, self.MyMath.subtraction_two_numbers(0, -5))

    def test_subtraction_zero_zero(self):
        self.assertEqual(0, self.MyMath.subtraction_two_numbers(0, 0))

    # test for multiplication
    def test_multiplication_positive_positive(self):
        self.assertEqual(14, self.MyMath.multiplication_two_numbers(2, 7))

    def test_multiplication_positive_negative(self):
        self.assertEqual(-7, self.MyMath.multiplication_two_numbers(7, -1))

    def test_multiplication_negative_positive(self):
        self.assertEqual(-7, self.MyMath.multiplication_two_numbers(-7, 1))

    def test_multiplication_positive_zero(self):
        self.assertEqual(0, self.MyMath.multiplication_two_numbers(11, 0))

    def test_multiplication_negative_zero(self):
        self.assertEqual(0, self.MyMath.multiplication_two_numbers(-8, 0))

    def test_multiplication_zero_positive(self):
        self.assertEqual(0, self.MyMath.multiplication_two_numbers(0, 6))

    def test_multiplication_zero_negative(self):
        self.assertEqual(0, self.MyMath.multiplication_two_numbers(0, -3))

    def test_multiplication_negative_negative(self):
        self.assertEqual(10, self.MyMath.multiplication_two_numbers(-5, -2))

    def test_multiplication_zero_zero(self):
        self.assertEqual(0, self.MyMath.multiplication_two_numbers(0, 0))

    # test for division
    def test_division_positive_positive(self):
        self.assertEqual(5, self.MyMath.division_two_numbers(10, 2))

    def test_division_positive_negative(self):
        self.assertEqual(-5, self.MyMath.division_two_numbers(5, -1))

    def test_division_zero_positive(self):
        self.assertEqual(0, self.MyMath.division_two_numbers(0, 2))

    def test_division_zero_negative(self):
        self.assertEqual(0, self.MyMath.division_two_numbers(0, -1))

    def test_division_negative_negative(self):
        self.assertEqual(6, self.MyMath.division_two_numbers(-24, -4))

    def test_division_negative_positive(self):
        self.assertEqual(-6, self.MyMath.division_two_numbers(-24, 4))

    def  test_division_positve_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.MyMath.division_two_numbers(5,0)

    def  test_division_negative_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.MyMath.division_two_numbers(-5,0)

    def  test_division_zero_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.MyMath.division_two_numbers(0,0)


if __name__ == '__main__':
    unittest.main()
