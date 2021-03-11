info = {}
time = []
qtgols = []
auxqtd = i = x = 0
esc = ''
det = ''
while True:
    info['nome'] = str(input('\nNome do jogador: ')).capitalize()
    n = input('Quantas partidas foram jogadas? ')
    while not n.isdigit():
        n = input('Por favor, digite um número: ')
    if n.isdigit():
        info['partidas'] = int(n)
        while auxqtd < info['partidas']:
            qtgols.append(int(input(f'  Quantos gols {info["nome"]} fez na {auxqtd+1}° partida: ')))
            auxqtd += 1
    info['gols'] = qtgols.copy()
    info['total'] = sum(qtgols)
    time.append(info.copy())

    esc = str(input('Quer continuar? [S/N]: ')).upper()[0]
    while esc not in 'SN':
        esc = str(input('Por favor, apenas Sim ou Não: ')).upper()[0]
    if esc == 'S':
        auxqtd = 0
        qtgols.clear()
        info.clear()
    elif esc == 'N':
        print()
        break
print(f'{"-" * 104}')
print(f'{" RESULTADO DO TIME ":^104}')
print(f'{"-" * 104}')
print(f'{"N°":^20}', end='')
for x in info.keys():
    print(f'|{x.upper():^20}', end='')
print()
print(f'{"-" * 104}')
for aux in time:
    print(f'{i+1:^20}', end='|')
    print(f'{aux["nome"]:^20}', end='|')
    print(f'{aux["partidas"]:^20}', end='|')
    print(f'{str(aux["gols"]):^20}', end='|')
    print(f'{aux["total"]:^20}')
    i += 1
    print(f'{"-" * 104}')
while True:
    det = ''
    j = 0
    if not det:
        det = input('\nQuer ver os dados de algum jogador?\n'
                    '[Sim = n° do jogador / Não = Qualquer letra ou número fora da lista dos jogadores: ')
        if not det.isdigit() or int(det) > len(time) or int(det) == 0:
            break
        else:
            det = int(det)-1
            print(f'\nLevantamento do jogador {time[det]["nome"]}')
            for c in time:
                while j < len(time[det]["gols"]):
                    print(f'    -> {j+1}° partida fez {time[det]["gols"][j]} gols')
                    j += 1
                if j == len(time[det]["gols"]):
                    break
print('\nPROGRAMA ENCERRADO!')
