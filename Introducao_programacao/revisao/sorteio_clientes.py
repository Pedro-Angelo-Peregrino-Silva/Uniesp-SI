# Uma empresa está realizando um sorteio para seus clientes.
# O programa deve gerar 10 números aleatórios entre 1 e 100.
# Os números sorteados devem ser impressos na tela.

from random import randint

lista_num_sorteados = list()
number = 0

while len(lista_num_sorteados) < 10:
    number = randint(1, 100)
    if number not in lista_num_sorteados:
        lista_num_sorteados.append(number)

print(lista_num_sorteados)
