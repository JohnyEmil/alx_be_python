import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class."""
    
    def setUp(self):
        """Set up test cases."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test addition operation."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, 8), 7)
        self.assertEqual(self.calc.add(1, 8), 9)
    
    def test_subtraction(self):
        """Test subtraction operation."""
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(1, -2), 3)
    
    def test_multiplication(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(5, 2), 10)
        self.assertEqual(self.calc.multiply(5, -2), -10)

    def test_division(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(2, 2), 1)
        self.assertEqual(self.calc.divide(6, 2), 3)

    def test_divide_by_zero(self):
        """Test division by zero raises appropriate error."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
