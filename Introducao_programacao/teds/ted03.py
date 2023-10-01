# questão 03

# a)
def letra_a():
    return print('Amo programar em Python!')


# b)
def letra_b():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    soma = num1 + num2
    return print(soma)


# c)
def letra_c():
    num = int(input('Digite um número: '))
    soma = num + 1357
    multi = soma * 8
    div = multi / 5
    potencia_dois = div ** 2
    return print(potencia_dois)


def letra_c_outro():
    num = int(input('Digite um número: '))
    calculo = (((num + 1357) * 8) / 5) ** 2
    return print(calculo)

# menu interativo
def linha(tamanho=60):
    return print('=' * tamanho)


def menu():
    print('''
    1 - Letra A
    2 - Letra B
    3 - Letra C
    4 - Letra C (outra opção)
    0 - Sair
    ''')
    while True:
        resp = str(input('Qual a sua escolha? ')).strip()[0]
        while resp not in '01234':
            resp = str(input('Qual a sua escolha? ')).strip()[0]
        if resp == '1':
            letra_a()
        elif resp == '2':
            letra_b()
        elif resp == '3':
            letra_c()
        elif resp == '4':
            letra_c_outro()
        else:
            print('Programa encerrado.')
            break


if __name__ == '__main__':
    menu()
