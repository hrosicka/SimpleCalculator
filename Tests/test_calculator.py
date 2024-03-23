import unittest
import sys
# setting path
sys.path.append('../PyQtSimpleCalculator')

from Calculator import Calculator, CalculatorError

class TestCalculator(unittest.TestCase):
    
    """
    This class contains unit tests for the Calculator class.

    These tests verify the functionality of the calculator's basic arithmetic 
    operations (addition, subtraction, multiplication, and division) for various 
    inputs, including:

    * Positive and negative numbers
    * Mixed combinations of positive and negative numbers
    * Zero values
    * Limit cases with very large or very small numbers

    The tests also ensure that division by zero raises a CalculatorError.
    """

    def test_add_positive(self):
        """
        Test that the add method returns the sum of two positive numbers.
        """
        calculator = Calculator()
        result = calculator.add(2.1, 2.5)
        self.assertEqual(result, 4.6)


    def test_add_negative(self):
        """
        Test that the add method returns the sum of two negative numbers.
        """
        calculator = Calculator()
        result = calculator.add(-2.1, -2.5)
        self.assertEqual(result, -4.6)


    def test_add_mixed(self):
        """
        Test that the add method returns the sum of a positive and a negative number.
        """
        calculator = Calculator()
        result = calculator.add(2.1, -2.1)
        self.assertEqual(result, 0.0)


    def test_add_zero(self):
        """
        Test that adding zero to any number returns the original number.
        """
        calculator = Calculator()
        result = calculator.add(0, 50)
        self.assertEqual(result, 50)

        result = calculator.add(50, 0)
        self.assertEqual(result, 50)


    def test_add_large_numbers(self):
        """
        Test that adding very large numbers does not cause overflow.
        """
        calculator = Calculator()
        result = calculator.add(1e100, 1)
        self.assertEqual(result, 1e100 + 1)


    def test_add_small_numbers(self):
        """
        Test that adding very small numbers does not lose precision.
        """
        calculator = Calculator()
        result = calculator.add(1e-100, 1e-100)
        self.assertEqual(result, 2e-100)



    def test_subtract_positive(self):
        """
        Test that the subtract method returns the difference of two positive numbers.
        """
        calculator = Calculator()
        result = calculator.subtract(5, 3)
        self.assertEqual(result, 2)


    def test_subtract_negative(self):
        """
        Test that the subtract method returns the difference of two negative numbers.
        """
        calculator = Calculator()
        result = calculator.subtract(-5, -3)
        self.assertEqual(result, -2)


    def test_subtract_mixed(self):
        """
        Test that the subtract method returns the difference of a positive and a negative number.
        """
        calculator = Calculator()
        result = calculator.subtract(111.111, -100)
        self.assertEqual(result, 211.111)


    def test_subtract_zero(self):
        """
        Test that subtracting zero from any number returns the original number.
        """
        calculator = Calculator()
        result = calculator.subtract(50, 0)
        self.assertEqual(result, 50)

        result = calculator.subtract(0, 50)
        self.assertEqual(result, -50)


    def test_subtract_large_numbers(self):
        """
        Test that subtracting very large numbers does not cause underflow.
        """
        calculator = Calculator()
        result = calculator.subtract(1e100, 1)
        self.assertEqual(result, 1e100 - 1)


    def test_subtract_small_numbers(self):
        """
        Test that subtracting very small numbers does not lose precision.
        """
        calculator = Calculator()
        result = calculator.subtract(1e-100, 1e-100)
        self.assertEqual(result, 0)


    def test_multiply_positive(self):
        """
        Test that the multiply method returns the product of two positive numbers.
        """
        calculator = Calculator()
        result = calculator.multiply(2.01, 4)
        self.assertEqual(result, 8.04)


    def test_multiply_negative(self):
        """
        Test that the multiply method returns the product of two negative numbers.
        """
        calculator = Calculator()
        result = calculator.multiply(-5.3, -2.0)
        self.assertEqual(result, 10.60)


    def test_multiply_mixed(self):
        """
        Test that the multiply method returns the product of a positive and a negative number.
        """
        calculator = Calculator()
        result = calculator.multiply(5.5, -3)
        self.assertEqual(result, -16.50)


    def test_multiply_zero(self):
        """
        Test that multiplying any number by zero returns zero.
        """
        calculator = Calculator()
        result = calculator.multiply(50, 0)
        self.assertEqual(result, 0)

        result = calculator.multiply(0, 50)
        self.assertEqual(result, 0)


    def test_multiply_large_numbers(self):
        """
        Test that multiplying very large numbers does not cause overflow.
        """
        calculator = Calculator()
        result = calculator.multiply(1e100, 1e10)
        self.assertEqual(result, 1e110)

    
    def test_multiply_small_numbers(self):
        """
        Test that multiplying very small numbers does not lose precision.
        """
        calculator = Calculator()
        result = calculator.multiply(1e-100, 1e-100)
        self.assertEqual(result, 1e-200)


    def test_divide_positive(self):
        """
        Test that the divide method returns the quotient of two positive numbers.
        """
        calculator = Calculator()
        result = calculator.divide(120, 3)
        self.assertEqual(result, 40)

    def test_divide_negative(self):
        """
        Test that the divide method returns the quotient of two negative numbers.
        """
        calculator = Calculator()
        result = calculator.divide(-1.2, -3)
        self.assertAlmostEqual(result, 0.4, places=5)

    def test_divide_mixed(self):
        """
        Test that the divide method returns the quotient of a positive and a negative number.
        """
        calculator = Calculator()
        result = calculator.divide(1.2, -3)
        self.assertAlmostEqual(result, -0.4, places=5)

    def test_divide_by_zero(self):
        """
        Test that dividing by zero raises a CalculatorError.
        """
        calculator = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(50, 0)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 0)


    def test_divide_large_numbers(self):
        """
        Test that dividing very large numbers does not cause underflow.
        """
        calculator = Calculator()
        result = calculator.divide(1e100, 1e10)
        self.assertEqual(result, 1e90)


    def test_divide_small_numbers(self):
        """
        Test that dividing very small numbers does not lose precision.
        """
        calculator = Calculator()
        result = calculator.divide(1e-100, 1e-100)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()