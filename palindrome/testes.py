import unittest
from palindrome import palindrome



class TestePalindrome5(unittest.TestCase):
    def test_fatorial(self):
        self.assertEqual(palindrome("asa"), True)

class TestePalindrome4(unittest.TestCase):
    def test_fatorial(self):
        self.assertEqual(palindrome("era pra ser erro"), "Parametro invalido")

class TestePalindrome3(unittest.TestCase):
    def test_fatorial(self):
        self.assertEqual(palindrome("marcelanderson"), False)

class TestePalindrome2(unittest.TestCase):
    def test_fatorial(self):
        self.assertEqual(palindrome(""), "Parametro invalido")

class TestePalindrome1(unittest.TestCase):
    def test_fatorial(self):
        self.assertEqual(palindrome("Appppa"), False)

class TestePalindrome0(unittest.TestCase):
    def test_fatorial(self):
        self.assertEqual(palindrome("245.5"), "Parametro invalido")

if __name__ == '__main__':
    unittest.main()