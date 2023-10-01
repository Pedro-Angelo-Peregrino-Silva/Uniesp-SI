# Escreva um programa que dê descontos de acordo com o valor da compra:
# acima de R$100, desconto de 10%;
# entre R$50 e R$100, desconto de 5%;
# abaixo de R$50, sem desconto.
# Calcule e mostre o valor do desconto e o valor total a pagar.


valor_compra = float(input('Digite o valor total das compras: R$ '))
valor_pagar = desconto = 0
if valor_compra > 100:
    desconto = (valor_compra * 10) / 100
    valor_pagar = valor_compra - desconto
    print(f'''
       O valor das compras foi de R$ {valor_compra:.2f}, com o desconto de 10% equivalente a {desconto},
       você irá pagar R$ {valor_pagar:.2f}.
       ''')
else:
    if valor_compra > 50:
        desconto = (valor_compra * 5) / 100
        valor_pagar = valor_compra - desconto
        print(f'''
           O valor das compras foi de R$ {valor_compra:.2f}, com o desconto de 5% equivalente a {desconto},
           você irá pagar R$ {valor_pagar:.2f}.
           ''')
    else:
        print(f'O valor das compras foi de R$ {valor_compra:.2f}, esse valor não possui desconto.')
