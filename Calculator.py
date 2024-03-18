class Calculator:
    """
    This class solves basic mathematical operations: 
    addition, subtraction, multiplication, and division.
    """
    def __init__(self):
        """
        This is the constructor for the Calculator class. It does not require any arguments.
        """
        pass

    def add(self, a, b):
        """
        This method adds two numbers and returns the sum of numbers.

        Args:
            a (float): The first number to be added.
            b (float): The second number to be added.

        Returns:
            float: The sum of a and b.
        """
        return a + b

    def subtract(self, a, b):
        """
        This method subtracts two numbers and returns the difference of numbers.

        Args:
            a (float): The first number from which the second number will be subtracted.
            b (float): The second number to be subtracted from the first number.

        Returns:
            float: The difference of a and b.
        """
        return a - b

    def multiply(self, a, b):
        """
        This method multiplies two numbers and returns the product of numbers.

        Args:
            a (float): The first number to be multiplied.
            b (float): The second number to be multiplied.

        Returns:
            float: The product of a and b.
        """
        return a * b

    def divide(self, a, b):
        """
        This method divides two numbers and returns the quotient of numbers.

        Args:
            a (float): The dividend (number to be divided).
            b (float): The divisor (number by which to divide).

        Raises:
            CalculatorError: If the divisor (b) is zero.

        Returns:
            float: The quotient of a and b.
        """
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b
    
class CalculatorError(Exception):
    pass