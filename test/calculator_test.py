""" Test cases for basic and scientific calculator
"""

# Importing modules
import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from app import calculator


class TestBasicCalculator(unittest.TestCase):
    """ Test cases for all potential scenarios for basic calculator
    """
    def setUp(self):
        """ Setup function for initializing the instance for basic calculator
        """
        super().__init__()
        self.cal = calculator.Calculator()

    def test_operation_add(self):
        """ Test the addition functionality of calculator
        """
        result, _ = self.cal.perform_operation('+', '3', '2')
        self.assertEqual(result, 5)

    def test_operation_sub(self):
        """ Test the subtraction functionality of calculator
        """
        result, _ = self.cal.perform_operation('-', '3', '2')
        self.assertEqual(result, 1)

    def test_operation_mul(self):
        """ Test the multiplication functionality of calculator
        """
        result, _ = self.cal.perform_operation('*', '3', '2')
        self.assertEqual(result, 6)

    def test_operation_div(self):
        """ Test the division functionality of calculator
        """
        result, _ = self.cal.perform_operation('/', '3', '2')
        self.assertEqual(result, 1.5)

    def test_empty_input(self):
        """ Test the scenario where both the inputs are empty
        """
        _, message = self.cal.perform_operation('+', '', '')
        self.assertEqual(message, "Please provide valid input.")

    def test_invalid_input(self):
        """ Test the scenario where invalid inputs are passed such as alphabets
        """
        _, message = self.cal.perform_operation('+', 'a', 'b')
        self.assertEqual(message, "Please provide valid input.")

    def test_division_by_zero(self):
        """ Test the division by zero operation, which raises an exception
        """
        _, message = self.cal.perform_operation('/', '7', '0')
        self.assertEqual(message, "Number 2 can't be zero. Please provide correct input.")


class TestScientificCalculator(unittest.TestCase):
    """ Test cases for all potential scenarios for scientific calculator
    """
    def setUp(self):
        """ Setup function for initializing the instance for scientific calculator
        """
        super().__init__()
        self.cal = calculator.ScientificCalculator()

    def test_operation_sin(self):
        """ Test the sine value of a number
        """
        result, _ = self.cal.perform_scientific_operation('sin', '3')
        self.assertEqual(result, 0.1411200080598672)

    def test_arithmetic_operation_sin(self):
        """ Test the sine of a number, on which arithmetic addition is performed
        """
        result, _ = self.cal.perform_scientific_operation('sin', '3', '2', '+')
        self.assertEqual(result, -0.9589242746631385)

    def test_operation_cos(self):
        """ Test the cosine value of a number
        """
        result, _ = self.cal.perform_scientific_operation('cos', '3')
        self.assertEqual(result, -0.9899924966004454)

    def test_operation_tan(self):
        """ Test the tangent value of a number
        """
        result, _ = self.cal.perform_scientific_operation('tan', '3')
        self.assertEqual(result, -0.1425465430742778)

    def test_operation_log(self):
        """ Test the logarithmic value of a number
        """
        result, _ = self.cal.perform_scientific_operation('log', '3')
        self.assertEqual(result, 1.0986122886681098)

    def test_empty_input(self):
        """ Test the scenario where both the inputs are empty
        """
        _, message = self.cal.perform_scientific_operation('sin', '', '')
        self.assertEqual(message, "Please provide valid input.")

    def test_invalid_input(self):
        """ Test the scenario where invalid inputs is passed such as alphabet
        """
        _, message = self.cal.perform_scientific_operation('sin', 'a')
        self.assertEqual(message, "Please provide valid input.")


if __name__ == '__main__':
    unittest.main()
