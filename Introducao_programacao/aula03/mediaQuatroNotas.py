# entrada de dados
n1, n2, n3, n4 = map(int, input('Digite 4 valores espaçados entre si: ').split())

media = (n1 + n2 + n3 + n4) / 4

print(f'O valor da média é {media}')
if media >= 7:
    print('O aluno está aprovado.')
else:
    if media >= 5:
        print('O aluno está em recuperação.')
    else:
        print('O aluno está reprovado!!')
