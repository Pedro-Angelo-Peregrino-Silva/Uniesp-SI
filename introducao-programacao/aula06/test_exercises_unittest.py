import unittest
from exercises import *


class Test_Exercises(unittest.TestCase):
    o = Calculadora()

    def test_soma(self):
        self.assertEqual(self.o.soma(num1=2, num2=2), 4)

    def test_subtracao(self):
        self.assertEqual(self.o.subtracao(num1=2, num2=2), 0)

    def test_divisao(self):
        self.assertEqual(self.o.divisao(num1=10, num2=2), 5)

    def test_multiplicacao(self):
        self.assertEqual(self.o.multiplicacao(num1=5, num2=5), 25)


if __name__ == '__main__':
    unittest.main()
