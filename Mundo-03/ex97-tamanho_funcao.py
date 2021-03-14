def mensagem(txt):
    print()
    print(f'{"-" * len(txt)}')
    print(txt)
    print(f'{"-" * len(txt)}')


for i in range(3):
    mensagem(txt=str(input('\nDigite o texto: ')))
