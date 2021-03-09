jogador = {'nome': str(input('Nome do jogador: ')),
           'partidas': int(input('Quantas partidas foram jogadas? '))
           }
i = 0
c = 0
qtd = []
while i < jogador['partidas']:
    qtd.append(int(input(f'Quantos gols {jogador["nome"]} fez na {i+1}° partida: ')))
    i += 1

jogador['gols'] = qtd
jogador['total'] = sum(jogador['gols'])

print(f'\n{" 1° RESULTADO ":-^32}')
for v in jogador:
    print(f'{v:^10} = {jogador[v]}')

print(f'\n{" 2° RESULTADO ":-^32}')
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for j in jogador['gols']:
    print(f'    => {c+1}° partida fez {jogador["gols"][c]} gols')
    c += 1
print(f'Total de gols foi {jogador["total"]}')
