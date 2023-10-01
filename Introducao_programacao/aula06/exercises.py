class Calculadora:
    def soma(self, num1, num2):
        return num1 + num2

    def subtracao(self, num1, num2):
        return num1 - num2

    def divisao(self, num1, num2):
        return num1 // num2

    def multiplicacao(self, num1, num2):
        return num1 * num2


if __name__ == '__main__':
    numero1 = int(input('Digite o 1° número:'))
    numero2 = int(input('Digite o 2° número:'))
    o = Calculadora()

    print(f'A soma de {numero1} + {numero2} = {o.soma(numero1, numero2)}')
    print(f'A subtração de {numero1} - {numero2} = {o.subtracao(numero1, numero2)}')
    print(f'A divisão de {numero1} / {numero2} = {o.divisao(numero1, numero2)}')
    print(f'A multiplicação de {numero1} * {numero2} = {o.multiplicacao(numero1, numero2)}')