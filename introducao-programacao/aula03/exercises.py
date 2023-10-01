from time import sleep


# questão 01:
def soma_2_numeros():
    '''
    Solicita 2 números e retorna a soma deles.
    '''
    num1, num2 = int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: '))
    soma = num1 + num2
    return print(f'A soma de {num1} + {num2} = {soma}')


# questão 02
def par_impar():
    '''
    Determina se o número é par ou ímpar
    '''
    num = int(input('Digite o número: '))
    if num % 2 == 0:
        resp = 'O número é par.'
    else:
        resp = 'O número é ímpar.'
    return print(resp)


# questão 03
def media_notas():
    nota1, nota2, nota3, nota4 = (int(input('Digite a notas: ')),
                                  int(input('Digite a notas: ')),
                                  int(input('Digite a notas: ')),
                                  int(input('Digite a notas: ')))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 7:
        return print('O aluno está aprovado.')
    else:
        return print('O aluno está reprovado.')


# questão 04
def idade_2025():
    nome, idade = str(input('Digite seu nome: ')), int(input('Digite a idade: '))
    idade += 2
    return print(f'{nome} terá em 2025 {idade} anos.')


# questão 05
def area_circulo():
    raio = float(input('Digite o raio do círculo em cm: '))
    area = 3.14 * raio ** 2
    return print(f'A área do circulo é {area:.2f} cm².')


# questão 06
def maior_menor_50():
    num = int(input('Digite um número: '))
    if num > 50:
        return print('O número digitado é MAIOR que 50.')
    elif num < 50:
        return print('O número digitado é MENOR que 50.')
    else:
        return print('O número digitado é IGUAL a 50.')


# questão 07
def divisao_erro():
    num1, num2 = int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: '))
    divisao = num1 // num2
    if num2 != 0:
        return print(f'A divisão de {num1} / {num2} = {divisao}')
    else:
        return print('ERRO: A divisão pelo número 0 não é viável.')


# questão 08
def maior_num():
    num1, num2, num3 = int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: '))
    list_nums = [num1, num2, num3]
    return print(f'O maior número digitado é {max(list_nums)}.')


# questão 09
def perimetro_circulo():
    raio = float(input('Digite o valor do raio: '))
    perimetro = 2 * 3.14 * raio
    return print(f'O perímetro do círculo é de {perimetro:.2f}')


# questão 10
def equacao_primeiro_grau():
    a, b, = int(input('Digite o valor de A: ')), int(input('Digite o valor de B:'))
    equacao = - b / a
    return print(f'o resultado da  equação de ax + b = 0 é de {equacao}, considerando a = {a} e b = {b}.')


def linha(tamanho=60):
    return print('=' * tamanho)


def menu():
    linha()
    print(f'{"LISTA DE EXERCÍCIOS 03":^60}')
    linha()
    print('''
    Questões:
    1  - Desconto na loja.
    2  - Desempenho funcionário.
    3  - Tipo triângulo.
    4  - Cinema
    5  - Condições climáticas.
    6  - Pesquisa eleitoral.
    7  - Cálculo de imposto.
    8  - Controle de velocidade.
    9  - Senha.
    10 - Equação primeiro grau.
    0 - Sair.
    ''')
    linha()


def main():
    while True:
        menu()
        resposta = int(input('Qual a opção escolhida: '))
        if resposta == 1:
            linha()
            soma_2_numeros()
            sleep(2)
        elif resposta == 2:
            linha()
            par_impar()
            sleep(2)
        elif resposta == 3:
            linha()
            media_notas()
            sleep(2)
        elif resposta == 4:
            linha()
            idade_2025()
            sleep(2)
        elif resposta == 5:
            area_circulo()
            sleep(2)
        elif resposta == 6:
            maior_menor_50()
            sleep(2)
        elif resposta == 7:
            divisao_erro()
            sleep(2)
        elif resposta == 8:
            maior_num()
            sleep(2)
        elif resposta == 9:
            perimetro_circulo()
            sleep(2)
        elif resposta == 10:
            equacao_primeiro_grau()
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
