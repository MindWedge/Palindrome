import unittest
from palindrome import is_palindrome
class TestPalindrome(unittest.TestCase):
    #1 raise error not provided string
    def test_value_error(self):
        with self.assertRaises(ValueError):
            is_palindrome(123)

	#2 return false if its empty
    def test_false_empty_string(self):
        self.assertFalse(is_palindrome(""))

    #3 return true with single character
    def test_true_single_character(self):
        self.assertTrue(is_palindrome("a"))

if __name__ == '__main__':
    unittest.main()
