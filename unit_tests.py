# cs362 - in class activity 04
# casey nord
# spring 2021


import unittest
from palindrome import *
from wordcount import *


class PalindromeUnitTests(unittest.TestCase):

    def test_correct_output(self):
        self.assertEqual(palindrome("racecar"), True)
        self.assertEqual(palindrome("tacocat"), True)
        self.assertEqual(palindrome("level"), True)
        self.assertEqual(palindrome("banana"), False)
    
    def test_type_handling(self):
        self.assertEqual(palindrome(42), -1)
        self.assertEqual(palindrome(26.4), -1)
        self.assertEqual(palindrome(False), -1)


if __name__ == '__main__':
    unittest.main()
