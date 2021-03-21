cores = ['\033[1;0m',   # 0 - Limpa
         '\033[1;31m',  # 1 - Vermelho
         '\033[1;32m',  # 2 - Verde
         '\033[1;34m',  # 3 - Azul
         '\033[1;33m',  # 4 - Amarelo
         '\033[1;36m',  # 5 - Ciano
         '\033[1;30m',  # 6 - Preto
         '\033[47m'     # 7 - Fundo Branco
         ]


def linha():
    print(f'{cores[5]}', end='')
    return print(f'{"-" * 50}{cores[0]}')

def titulo(msg):
    linha()
    print(f'{cores[5]}{msg:^50}')
    linha(), cores[0]


def leint(msg):
    """
    -> Testa se um número é int, em looping até se inputado um int.
    :param msg: mensagem de input
    :return: resultado do teste.
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'{cores[1]}Escolha apenas uma das opções do menu!{cores[0]}')
            return 0
        else:
            return n


def menu(lista):
    titulo(f'MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\t{cores[5]}{c} - {cores[0]}{item}')
        c += 1
    linha()
    opc = leint(f'{cores[4]}Sua Opção: {cores[0]}')
    return opc
