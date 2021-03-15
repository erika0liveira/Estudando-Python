def ficha(nome='desconhecido', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato')


n = input('Digite o nome do jogador: ')
g = input('Digite a quantidade de gols: ')
if g.isnumeric():
    int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
