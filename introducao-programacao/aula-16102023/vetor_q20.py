# Desenvolva um programa para ler um vetor Q de 20 posições
# (aceitar somente números positivos). Escrever a seguir:
# o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
# o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;


lista_numeros = list()
posicao_maior = posicao_menor = 0
maior_numero = menor_numero = ''


while len(lista_numeros) <= 19:
    numero_lista = int(input('Digite um número: '))
    while numero_lista < 0:
        numero_lista = int(input('Digite um número positivo: '))
    if numero_lista not in lista_numeros:
        lista_numeros.append(numero_lista)
        if len(lista_numeros) == 1:
            maior_numero = menor_numero = int(numero_lista)
    else:
        print(f'Esse número já está inserido no conjunto.')

for numero in range(0, len(lista_numeros)):
    if maior_numero < lista_numeros[numero]:
        maior_numero = lista_numeros[numero]
        posicao_maior = numero
    if menor_numero > lista_numeros[numero]:
        menor_numero = lista_numeros[numero]
        posicao_menor = numero

print(f'O maior elemento da lista é {maior_numero} sendo sua posição na lista {posicao_maior}.')
print()
print(f'O menor elemento da lista é {menor_numero} sendo sua posicao na lista {posicao_menor}')




