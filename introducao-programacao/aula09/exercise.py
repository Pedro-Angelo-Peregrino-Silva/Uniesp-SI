# Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos
# em um vetor (lista).
# Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI,
# se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.


lista_clubes = [
    ['Flamengo'], ['Vasco'], ['Santos'], ['Grêmio'], ['ABC'], ['Curitiba'], ['Atlético-Minéiro'],
    ['Nacional de Patos'], ['Fluminense'], ['Botafogo-PB'], ['Botafogo'], ['Bragantino'], ['Palmeiras'],
    ['São Paulo'], ['Cuiaba'], ['Internacional'], ['Corinthians'], ['Cruzeiro'], ['Bahia'], ['Vitória'],
    ['13 de Campina Grande']
    ]


def busca(lista, elemento):
    for i in range(0, len(lista)):
        nome = lista[i]
        if nome in lista:
            return i
        else:
            return False


if __name__ == '__main__':
    elemento_procurado = str(input('Digite o nome do clube: '))

    indice = busca(lista_clubes, elemento_procurado)

    if indice is not False:
        print(f'O time {elemento_procurado} encontrado na posição {indice} da lista de Clubes.')
    else:
        print(f'O time {elemento_procurado} não se encontra na lista.')


