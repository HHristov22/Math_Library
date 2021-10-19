class InvalidType(Exception):
    """Class for exceptions for invalid type"""
    pass


class ZeroDivisionError(Exception):
    """Class for exceptions for divide by zero"""
    pass


def is_integer(var):
    """
    Check the var is integer
    """
    if type(var) != int:
        return False
    else:
        return True


class MyMath:
    """
    A python class 'my_math' for basic arithmetic operations.
    The class can be used for:
    Addition, subtraction, multiplication and division.
    """

    def addition_two_numbers(self, x, y) -> int:
        """
        Add two numbers.
        Input: X: (int type)
        Input Y: (int type)
        Return: X + Y (int type)
        """
        if is_integer(x) and is_integer(y):
            return x + y
        else:
            raise InvalidType(
                'The input is invalid. Input needs to be integer.')

    def subtraction_two_numbers(self, x, y) -> int:
        """
        Add two numbers.
        Input: X: (int type)
        Input Y: (int type)
        Return: X + Y (int type)
        """
        if is_integer(x) and is_integer(y):
            return x - y
        else:
            raise InvalidType(
                'The input is invalid. Input needs to be integer.')

    def multiplication_two_numbers(self, x, y) -> int:
        """
        Subtraction of two numbers.
        Input: X: (int type)
        Input Y: (int type)
        Return: X * Y (int type)
        """
        if is_integer(x) and is_integer(y):
            return x * y
        else:
            raise InvalidType(
                'The input is invalid. Input needs to be integer.')

    def division_two_numbers(self, x, y) -> int:
        """
        Division of two numbers.
        Input: X: (int type)
        Input Y: (int type)
        Return: X / Y (double type)
        """
        if is_integer(x) and is_integer(y):
            if y == 0:
                raise ZeroDivisionError(
                    'Second input is 0. You can\'t divide by 0.')
            else:
                return x / y
        else:
            raise InvalidType(
                'The input is invalid. Input needs to be integer.')


"""
import unittest

def t():
    return 9/0

class TestT(unittest.TestCase):
    def setUp(self):
        self.t = t()

    def tearDown(self):
        del self.t

    def test_t():
        # with self.assertRaises(ZeroDivisionError):
        #     t()
        self.assertEqual(7, self.t())"""
