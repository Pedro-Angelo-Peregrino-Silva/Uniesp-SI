# questão 01
def positivo_negativo():
    numero = float(input('Digite um número: '))
    if numero >= 0:
        msg = f'O número {numero} é positivo.'
        return print(msg)

    else:
        msg = f'O número {numero} é negativo'
        return msg


# questão 02
def compra_maca():
    num_maca = int(input('Digite quantas maçãs você irá comprar? '))
    if num_maca < 12:
        total_pagar = num_maca * 1.30
    else:
        total_pagar = num_maca * 1

    return print(f'Você comprou {num_maca} maçãs, o valor total da compra é de R$ {total_pagar:.2f}')


def menu():
    print('''
    1 - Número positivo / negativo
    2 - Compra maçãs
    0 - Sair
    ''')
    while True:
        resp = str(input('Qual a sua escolha? ')).strip()[0]
        while resp not in '012':
            resp = str(input('Qual a sua escolha? ')).strip()[0]
        if resp == '1':
            positivo_negativo()
        elif resp == '2':
            compra_maca()
        else:
            print('Programa encerrado.')
            break


if __name__ == '__main__':
    menu()
