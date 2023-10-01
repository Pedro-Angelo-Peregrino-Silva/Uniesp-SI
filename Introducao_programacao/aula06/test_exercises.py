from exercises import *


class Test_Exercises:
    o = Calculadora()

    def test_soma(o):
        assert o.soma( 2, 2) == 4

    def test_subtracao():
        assert o.subtracao(2, 2) == 0

    def test_divisao():
        assert o.divisao(10, 2) == 5

    def test_multiplicacao():
        assert o.multiplicacao(5, 5) == 25


if __name__ == '__main__':
    o = Test_Exercises
    o()
