from time import sleep


# questão 01
def maior_10():
    num = float(input('Digite um número: '))
    if num > 10:
        return print(f'Maior.')
    else:
        return print(f'Menor.')


# questão 02
def avaliacao_1_2():
    nota1, nota2 = float(input('Digite a 1° nota: ')), float(input('Digite a 2° nota: '))
    media = (nota1 + nota2) / 2
    if media >= 6:
        return print(f'Sua média foi de {media}, você está Aprovado!')
    else:
        return print(f'Sua média foi de {media}, você está Reprovado!')


# questão 03
def maior_valor():
    valor1, valor2 = 1, 2
    lista_valores = []
    while valor1 != valor2:
        valor1, valor2 = int(input('Digite um número: ')), int(input('Digite um número: '))
        if valor1 != valor2:
            lista_valores.appedn(valor1)
            lista_valores.appedn(valor2)
    return print(max(lista_valores))


# questão 04
def ordem_valor():
    valor1, valor2 = 1, 2
    lista_valores = []
    while valor1 != valor2:
        valor1, valor2 = int(input('Digite um número: ')), int(input('Digite um número: '))
        if valor1 != valor2:
            lista_valores.appedn(valor1)
            lista_valores.appedn(valor2)
    return print(lista_valores.sort())


# questão 05
def valores_conta_corrente():
    num_cc, saldo_cc, debito_cc, credito_cc = (int(input('Digite o número da Conta-Corrente: ')),
                                               float(input('Digite o saldo da sua CC: ')),
                                               float(input('Digite o débito da sua CC: ')),
                                               float(input('Digite o crédito da sua CC: ')))
    saldo_atual = saldo_cc - debito_cc + credito_cc

    if saldo_atual >= 0:
        saldo_p_n = 'POSITIVO'
    else:
        saldo_p_n = 'NEGATIVO'

    return print(f'''
O saldo atual é de : R$ {saldo_atual}.
Seu saldo está {saldo_p_n}.
''')


# questão 06
def verificacao_estoque():
    estoque_atual, estoque_max, estoque_min = (int(input('Digite o número da Conta-Corrente: ')),
                                               int(input('Digite o saldo da sua CC: ')),
                                               int(input('Digite o débito da sua CC: ')))

    estoque_media = (estoque_max + estoque_min) / 2

    if estoque_atual >= estoque_media:
        return print('Não efetuar compra.')
    else:
        return print('Efetuar compra.')


# questão 07
def desconto_compra():
    valor_compra = float(input('Digite o valor total das compras: R$ '))
    valor_pagar = desconto = 0
    if valor_compra > 100:
        desconto = (valor_compra * 10) / 100
        valor_pagar = valor_compra - desconto
        return print(f'''
        O valor das compras foi de R$ {valor_compra:.2f}, com o desconto de 10% equivalente a {desconto}, você irá pagar R$ {valor_pagar:.2f}.
        ''')
    else:
        if valor_compra > 50:
            desconto = (valor_compra * 5) / 100
            valor_pagar = valor_compra - desconto
            return print(f'''
            O valor das compras foi de R$ {valor_compra:.2f}, com o desconto de 5% equivalente a {desconto}, você irá pagar R$ {valor_pagar:.2f}.
            ''')
        else:
            return print(f'O valor das compras foi de R$ {valor_compra:.2f}, esse valor não possui desconto.')


# questão 08
def avaliacao_funcionarios():
    hora_extra, hora_falta = (int(input('Digite a quantidade de horas extras: ')),
                              int(input('Digite a quantidade de horas faltadas: ')))
    hora_falta_50 = hora_falta + (hora_falta//2)

    if hora_extra >= hora_falta_50:
        return print('Bônus de R$ 500,00.')
    else:
        return print('Sem bônus.')


# questao 9
def tipo_triangulo():
    lado1, lado2, lado3 = (float(input('Digite o lado A do triângulo: ')),
                           float(input('Digite o lado B do triângulo: ')),
                           float(input('Digite o lado C do triângulo: ')))
    if lado1 == lado2 == lado3:
        return print('O triângulo é equilátero, ou seja, todos os lados são iguais.')
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        return print('O triângulo é isósceles, ou seja, possue dois lados iguais.')
    else:
        return print('O triângulo é escaleno, ou seja, todos os lados são diferentes.')


# questão 10
def idade_cinema():
    idade_user = int(input('Qual a sua idade? '))
    if 12 >= idade_user >= 60:
        return print('O valor do ingresso é de R$ 25,00.')
    else:
        return print('O valor do ingresso é de R$ 15,00.')


# questão 11
def condicao_climatica():
    temp_atual = float(int('Informe a temperatura atual: '))
    if temp_atual < 15:
        return print('O clima está frio.')
    elif 15 <= temp_atual <= 25:
        return print('O clima está ameno.')
    else:
        return print('O clima está quente.')


# questão 12
def pesquisa_eleitoral():
    print('''
    Candidatos disponíveis:
    1 - Candidato A
    2 - Candidato B
    3 - Candidato C
    * - Voto nulo
    
    "*" Significa qualquer outro número para votar nulo.
    ''')
    voto = str(input('Qual seu voto? ')).strip()[0]
    if voto in '123':
        if voto == '1':
            return print('Você votou no candidato A.')
        elif voto == '2':
            return print('Você votou no candidato B.')
        else:
            return print('Você votou no candidato C.')
    else:
        return print('Você votou NULO!')


# questão 13
def calculo_imposto():
    salario = float(input('Informe seu rendimento mensal: R$ '))
    if salario <= 2000:
        return print('Você está isento de impostos.')
    elif 2000.1 <= salario <= 3500:
        return print('Você pagará 10% de imposto de renda.')
    else:
        return print('Você pagará 15% de imposto de renda.')


# questão 14
def speed_control():
    speed = float(input('Digite a velocidade atual do veículo: '))
    if speed <= 80:
        return print(f'Sua velocidade é de {speed} km/h, você está abaixo do limite de velocidade permitido.')
    else:
        multa = (speed - 80) * 5
        return print(f'Você se encontra acima da velocidade permitida, sua multa será no valor de R$ {multa:.2f}.')

# questão 15
def password_system():
    print('Usuário: PYTHON')
    password = str(input('Senha: ')).strip()
    while password != 'Python123':
            password = str(input('Senha ERRADA!!! Digite a senha novamente: '))
    return print('Acesso CONCEDIDO.')


def linha(tamanho=60):
    return print('=' * tamanho)


def menu():
    linha()
    print(f'{"LISTA DE EXERCÍCIOS 04":^60}')
    linha()
    print('''
    Questões:
    1  - Maior que 10.
    2  - Avaliação entre 2 números.
    3  - Maior valor.
    4  - Ordenação de valores.
    5  - Valores Conta Corrente.
    6  - Controle de Estoque.
    7  - Desconto na loja.
    8  - Desempenho funcionário.
    9  - Tipo triângulo.
    10 - Cinema
    11 - Condições climáticas.
    12 - Pesquisa eleitoral.
    13 - Cálculo de imposto.
    14 - Controle de velocidade.
    15 - Senha.
    0 - Sair.
    ''')
    linha()


def main():
    while True:
        menu()
        resposta = int(input('Qual a opção escolhida: '))
        if resposta == 1:
            linha()
            maior_10()
            sleep(2)
        elif resposta == 2:
            linha()
            avaliacao_1_2()
            sleep(2)
        elif resposta == 3:
            linha()
            maior_valor()
            sleep(2)
        elif resposta == 4:
            linha()
            ordem_valor()
            sleep(2)
        elif resposta == 5:
            linha()
            valores_conta_corrente()
            sleep(2)
        elif resposta == 6:
            linha()
            verificacao_estoque()
            sleep(2)
        elif resposta == 7:
            linha()
            desconto_compra()
            sleep(2)
        elif resposta == 8:
            linha()
            avaliacao_funcionarios()
            sleep(2)
        elif resposta == 9:
            linha()
            tipo_triangulo()
            sleep(2)
        elif resposta == 10:
            linha()
            idade_cinema()
            sleep(2)
        elif resposta == 11:
            condicao_climatica()
            sleep(2)
        elif resposta == 12:
            pesquisa_eleitoral()
            sleep(2)
        elif resposta == 13:
            calculo_imposto()
            sleep(2)
        elif resposta == 14:
            speed_control()
            sleep(2)
        elif resposta == 15:
            password_system()
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




