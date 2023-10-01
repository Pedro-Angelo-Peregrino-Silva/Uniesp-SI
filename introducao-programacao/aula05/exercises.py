from time import sleep


def linha(tamanho=60):
    print('=' * tamanho)


# questão 1
def divisao_resto5():
    for i in range(1000, 2000):
        if i % 11 == 11:
            print(i)


# questão 2
def tabuada_1_10():
    for i in range(1, 11):
        linha()
        for j in range(1, 11):
            resultado = i * j
            print(f'{i} x {j} = {resultado}')


# questão 3
def lista_amigo():
    lista_amigos = []
    while True:
        nome = str(input('Digite o nome de um amigo: ')).capitalize().strip()
        lista_amigos.append(nome)
        resp = str(input('Deseja cadastrar outro nome?[S/N]')).strip()[0]
        while resp not in 'SsNn':
            resp = str(input('Deseja cadastrar outro nome?[S/N]')).strip()[0]
        if resp in 'Nn':
            break
    for i in range(0, len(lista_amigos)):
       return print(f'{lista_amigos[i]}')


# questão 4
def tabuada_user():
    num = int(input('Digite um número: '))
    for i in range(1, 11):
        resultado = num * i
        return print(f'{num} x {i} = {resultado}')


# questão 5
def lista_amigo_saudacao():
    lista_amigos = []
    while True:
        nome = str(input('Digite o nome de um amigo: ')).capitalize().strip()
        lista_amigos.append(nome)
        resp = str(input('Deseja cadastrar outro nome?[S/N]')).strip()[0]
        while resp not in 'SsNn':
            resp = str(input('Deseja cadastrar outro nome?[S/N]')).strip()[0]
        if resp in 'Nn':
            break
    for i in range(0, len(lista_amigos)):
        return print(f'Olá, como vai você {lista_amigos[i]}?')


# questão 6
def festa_casa():
    lista_celebridades = []
    celebridades_confirmadas = []
    celebridades_n_confirmadas = []

    # Cadastro dos participantes
    while True:
        nome = str(
            input('Digite o nome de uma celebridade: ')).capitalize().strip()
        lista_celebridades.append(nome)
        resp = str(input('Deseja cadastrar outro nome?[S/N]')).strip()[0]
        while resp not in 'SsNn':
            resp = str(input('Deseja cadastrar outro nome?[S/N]')).strip()[0]
        if resp in 'Nn':
            break

    # confirmação e exclusão dos não presentes
    for i in range(0, len(lista_celebridades)):
        confirmacao = str(
            input(f'Olá, {lista_celebridades[i]}, Você irá a minha festa?[S/N] ')
        ).strip()[0]
        if confirmacao not in 'Ss':
            celebridades_n_confirmadas.append(lista_celebridades[i])
        else:
            celebridades_confirmadas.append(lista_celebridades[i])

    # Lista dos presentes
    print('A lista das celebridades que irão:')
    for i in range(len(celebridades_confirmadas)):
        return print(f'{celebridades_confirmadas[i]}')

    # Lista dos NÃO presentes
    print('A lista das celebridades que NÃO irão:')
    for i in range(len(celebridades_n_confirmadas)):
        return print(f'{celebridades_n_confirmadas[i]}')


# questão 07
def cadastro_client():
    lista_client = list()
    lista_cadastros = list()
    while True:
        linha()
        # cadastro do nome
        nome_client = str(input('Nome: ')).strip().capitalize()
        lista_client.append(nome_client)
        # cadastro da idade
        idade_client = int(input('Idade: '))
        lista_client.append(idade_client)
        # cadastro do email
        email_client = str(input('email: ')).strip()
        lista_client.append(email_client)
        # Cadastro de dados da lista_client na lista_cadastros
        lista_cadastros.append(lista_client[:])
        lista_client.clear()

        resposta = str(input('Cadastrar outro?[S/N] ')).strip().upper()[0]
        while resposta not in 'SN':
            resposta = str(input('Cadastrar outro?[S/N] ')).strip().upper()[0]
        if resposta == 'N':
            print('Encerrando programa...')
            sleep(2)
            print('Programa encerrado!')
            linha()
            # imprimir os cadastros
            for i in range(len(lista_cadastros)):
                for j in range(len(lista_cadastros[i])):
                    return print(f'{lista_cadastros[i][j]}')
                linha()

            break


def menu():
    linha()
    print(f'{"LISTA DE EXERCÍCIOS 04":^60}')
    linha()
    print('''
  Questões:
  1  - divisão resto 5.
  2  - tabuada de 1 a 10.
  3  - lista de amigos.
  4  - tabuada com entrada do número.
  5  - lista de amigos com saudação.
  6  - festa em casa.
  7  - cadastro de clientes.
  0 - Sair.
  ''')
    linha()


def main():
    while True:
        menu()
        resposta = int(input('Qual a opção escolhida: '))
        if resposta == 1:
            linha()
            divisao_resto5()
            sleep(2)
        elif resposta == 2:
            linha()
            tabuada_1_10()
            sleep(2)
        elif resposta == 3:
            linha()
            lista_amigo()
            sleep(2)
        elif resposta == 4:
            linha()
            tabuada_user()
            sleep(2)
        elif resposta == 5:
            linha()
            lista_amigo_saudacao()
            sleep(2)
        elif resposta == 6:
            linha()
            festa_casa()
            sleep(2)
        elif resposta == 7:
            linha()
            cadastro_client()
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
