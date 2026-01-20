import unittest
from main import is_palindrome

class TestPalidrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("RaceCar"))

if __name__ == "__main__":
    unittest.main()