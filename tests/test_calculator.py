import unittest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator_memory import Calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up a fresh calculator for each test."""
        self.calc = Calculator()
    
    def test_initial_state(self):
        """Test initial memory and history state."""
        self.assertEqual(self.calc.memory, 0)
        self.assertEqual(self.calc.history, [])
    
    def test_basic_operations(self):
        """Test basic arithmetic operations."""
        # Addition
        self.assertEqual(self.calc.add(5, 3), 8)
        
        # Subtraction
        self.assertEqual(self.calc.subtract(10, 4), 6)
        
        # Multiplication
        self.assertEqual(self.calc.multiply(6, 7), 42)
        
        # Division
        self.assertEqual(self.calc.divide(15, 3), 5)
        
        # Power
        self.assertEqual(self.calc.power(2, 3), 8)
    
    def test_division_by_zero(self):
        """Test division by zero error handling."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_square_root(self):
        """Test square root operation."""
        self.assertEqual(self.calc.square_root(25), 5)
        self.assertEqual(self.calc.square_root(0), 0)
    
    def test_square_root_negative(self):
        """Test square root of negative number error."""
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
    
    def test_memory_operations(self):
        """Test memory storage and recall."""
        self.calc.store_memory(100)
        self.assertEqual(self.calc.recall_memory(), 100)
        
        self.calc.add_to_memory(50)
        self.assertEqual(self.calc.memory, 150)
        
        self.calc.subtract_from_memory(30)
        self.assertEqual(self.calc.memory, 120)
        
        self.calc.clear_memory()
        self.assertEqual(self.calc.memory, 0)
    
    def test_memory_based_calculations(self):
        """Test calculations using memory."""
        self.calc.store_memory(10)
        
        # Memory-based addition
        result = self.calc.add(5)  # Should be M + 5 = 15
        self.assertEqual(result, 15)
        
        # Memory-based multiplication
        result = self.calc.multiply(3)  # Should be M * 3 = 30
        self.assertEqual(result, 30)
    
    def test_history(self):
        """Test calculation history."""
        self.calc.add(2, 3)
        self.calc.subtract(10, 4)
        self.calc.store_memory(100)
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 3)
        self.assertIn("2 + 3 = 5", history[0])
        self.assertIn("10 - 4 = 6", history[1])
        self.assertIn("Store 100 in memory", history[2])
        
        self.calc.clear_history()
        self.assertEqual(len(self.calc.get_history()), 0)

if __name__ == '__main__':
    unittest.main()