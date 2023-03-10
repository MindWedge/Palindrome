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

    #4 return true with two character
    def test_true_two_character(self):
        self.assertTrue(is_palindrome("bb"))

    #5 return false with three character
    def test_false_three_character(self):
        self.assertFalse(is_palindrome("abc"))

    #6 return true for laval
    def test_true_for_laval(self):
        self.assertTrue(is_palindrome("laval"))
        
    #7 return false for toronto
    def test_true_for_toronto(self):
        self.assertFalse(is_palindrome("toronto"))
        
    #8 return true for string
    def test_true_for_string(self):
        self.assertTrue(is_palindrome("Able was I ere I saw Elba"))

if __name__ == '__main__':
    unittest.main()
