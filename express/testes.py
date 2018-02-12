import unittest
from validador import validador_parenteses

class TesteValidador(unittest.TestCase):
    def test_validador_true(self):
        self.assertEqual(validador_parenteses("()"), True)

    def test_validador_false(self):
        self.assertEqual(validador_parenteses(")"), False)

    def test_validador_false2(self):
        self.assertEqual(validador_parenteses("())"), False)

    def test_validador_false3(self):
        self.assertEqual(validador_parenteses("("), False)

    def test_validador_true2(self):
        self.assertEqual(validador_parenteses("()()"), True)

    def test_validador_true3(self):
        self.assertEqual(validador_parenteses("(()())"), True)

    def test_validador_false4(self):
        self.assertEqual(validador_parenteses(")()("), False)

if __name__ == '__main__':
    unittest.main()