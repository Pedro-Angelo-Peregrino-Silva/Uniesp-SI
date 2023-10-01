# Uma empresa está realizando uma pesquisa de satisfação com seus clientes.
# O programa deve solicitar ao usuário a sua nota de satisfação com a empresa, de 1 a 5.
# O programa deve imprimir o número de clientes que avaliaram a empresa com cada nota.


notas_clientes = list()

while True:
    nota_satisfacao = str(input('Qual a sua nota para nosso atendimento?[1-5] ')).strip()[0]
    if nota_satisfacao not in '12345':
        nota_satisfacao = str(input('Qual a sua nota para nosso atendimento?[1-5] ')).strip()[0]
    else:
        notas_clientes.append(nota_satisfacao)
    resp = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O número de clientes que votaram 5 é {notas_clientes.count("5")}')
print(f'O número de clientes que votaram 4 é {notas_clientes.count("4")}')
print(f'O número de clientes que votaram 3 é {notas_clientes.count("3")}')
print(f'O número de clientes que votaram 2 é {notas_clientes.count("2")}')
print(f'O número de clientes que votaram 1 é {notas_clientes.count("1")}')
