from Tratamento_Erros.ex115.lib.arquivo import *

arq = 'cadastro.txt'

if not arqexiste(arq):
    criararq(arq)
while True:
    e = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if e == 1:
        lerarq(arq)
    elif e == 2:
        titulo("CADASTRAR NOVA PESSOA")
        nome = str(input('Nome: ')).title().strip()
        idade = leint('Idade: ')
        cadastrar(arq, nome, idade)
    elif e == 3:
        titulo("SAINDO DO SISTEMA... ATÉ LOGO")
        break
    else:
        print(f'{cores[1]}Escolha apenas uma das opções do menu!{cores[0]}')
