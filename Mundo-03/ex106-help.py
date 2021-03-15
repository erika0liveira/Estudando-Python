from time import sleep

cores = ('\033[0;0m',   # 0 - Limpa
         '\033[1;40m',  # 1 - Fundo Preto
         '\033[1;41m',  # 2 - Fundo vermelho
         '\033[1;42m ', # 3 - Fundo Verde
         '\033[1;46m',  # 4 - Fundo Ciano
         )


def titulo(msg, cor=0):
    print(cores[cor], end='')
    print(f'~' * len(msg))
    print(f'{msg}')
    print(f'~' * len(msg))
    print(cores[0])


def ajuda(com):
    titulo(f'Acessando o manual do comando {com}', 4)
    print(cores[1], end='')
    sleep(1)
    help(com)
    print(cores[0])


while True:
    titulo('SISTEMA DE AJUDA PYHELP', 3)
    escolha = input(f'Função ou Biblioteca (Fim para encerrar): ')
    if escolha.upper() == 'FIM':
        break
    else:
        ajuda(escolha)
titulo('ATÉ LOGO', 2)
