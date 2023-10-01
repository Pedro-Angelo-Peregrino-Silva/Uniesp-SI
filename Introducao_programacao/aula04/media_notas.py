# Entrada de dados
nota1, nota2 = float(input('Digite a primeira nota: ')), float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 6:
    print(f'A média foi {media:.1f}, aluno APROVADO!!')
elif media >= 4:
    print(f'A média foi {media:.1f}, o aluno está em recuperação.')
else:
    print(f'O aluno está reprovado.')
    