from ted04 import positivo_negativo


def test_positivo_negativo():
    assert positivo_negativo(0) == 'O número 0 é positivo.'
    assert positivo_negativo(-1) == 'O número -1 é negativo'
