
glossario = (
    {'algoritmos': 'Em matemática e ciência da computação, um algoritmo é uma sequência finita de ações executáveis que '
                   'visam obter uma solução para um determinado tipo de problema.[1][2] Segundo Dasgupta, Papadimitriou '
                   'e Vazirani; "Algoritmos são procedimentos precisos, não ambíguos, padronizados, eficientes e corretos."'},
    {'python': 'é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos,'
               ' funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.'},
    {'webscraping': 'A coleta de dados web, ou raspagem web, é uma forma de mineração que permite a extração de dados de'
                    ' sites da web convertendo-os em informação estruturada para posterior análise'},
    {'lógica de programação': 'é o elemento essencial para o processo de desenvolvimento de software. '
                              'É ela quem organiza de maneira coerente a sequência de ações que um algoritmo precisa executar.'},
    {'google colab': 'é um ambiente de notebooks Jupyter que não requer configuração e é executado na nuvem do Google.'},
    {'visual studio code': 'Um editor de código-fonte autônomo que é executado no Windows, macOS e Linux. '
                           'A melhor escolha para desenvolvedores JavaScript e Web, com toneladas de extensões dar suporte '
                           'a praticamente qualquer linguagem de programação'}
)

for index in glossario:
    for chaves in index.keys():
        print(f'* {chaves}:')
        for definition in index.values():
            print(f'    {definition}.')
            print()

