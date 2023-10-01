# Faça um programa que mostre as tabuadas dos números de 1 a 10.
# Escreva o programa em Python, entregue:
# Pseudocódigo;
# Fluxograma;
# E código Python em .py ou .ipynb.

# tabuada de 1 a 10
for i in range(1, 11):
    for j in range(1, 11):
        resultado = i * j
        print(f'{i} x {j} = {resultado}')
    print(f'=' * 60)
