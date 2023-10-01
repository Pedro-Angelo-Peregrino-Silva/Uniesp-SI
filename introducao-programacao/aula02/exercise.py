from time import sleep


# questão 01
def calculos_variados():
    num_usuario = int(input('Digite um número: '))
    calculo = (((num_usuario + 1357) * 8) / 5) **2
    msg = f'O resultado da soma de ({num_usuario} + 1357 x 8)² = {calculo}'
    return print(msg)


# questão 02
def convite_festa():
    nome = str(input('Digite o nome do aniversariante: ')).upper()
    msg = f'Venho aqui convida-lo para o meu aniversário. ass.: {nome}.'
    return print(msg)


# questão 03
def calculo_oito():
    soma = 4 + 4
    multiplicacao = 2 * 4
    divisao = 16 / 2
    subtracao = 16 - 8

    return print(f'''
    A soma de 4 + 4 = {soma}
    A multiplicação de 2 x 4 = {multiplicacao}
    A divisão de 16 / 2 = {divisao}
    A subtração de 16 - 8 = {subtracao}
    ''')


def linha(tamanho=60):
    return print('=' * tamanho)


def menu():
    linha()
    print(f'{"LISTA DE EXERCÍCIOS 02":^60}')
    linha()
    print('''
    Questões:
    1  - Calculos variados.
    2  - Convite festa.
    3  - Resultado das operções é 8.
    0 - Sair.
    ''')
    linha()


def main():
    while True:
        menu()
        resposta = int(input('Qual a opção escolhida: '))
        if resposta == 1:
            linha()
            calculos_variados()
            sleep(2)
        elif resposta == 2:
            linha()
            convite_festa()
            sleep(2)
        elif resposta == 3:
            linha()
            calculo_oito()
            sleep(2)
        elif resposta == 0:
            linha()
            print('Encerrando........')
            sleep(2)
            print('Programa encerrado.')
            break
        else:
            print('Opção inválida!')


if __name__ == '__main__':
    main()
