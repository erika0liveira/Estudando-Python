from Tratamento_Erros.ex115.lib.design import *


def arqexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarq(nome):
    try:
        a = open(nome, 'rt')
    except IndexError:
        print('Erro ao ler o arquivo!')
    else:
        titulo("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'Nome: {dado[0]:<30}Idade:{dado[1]:>3}')
    finally:
        a.close()


def cadastrar(arq, nome="Desconhecido", idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {cores[3]}{nome.title()}{cores[0]} adicionado com sucesso!')
