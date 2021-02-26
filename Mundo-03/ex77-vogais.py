palavras = ('palavras', 'aleatorios', 'vogais', 'consoantes', 'abstrato', 'logica', 'programaçao',
            'cafe', 'bolo', 'brownie', 'cha', 'pao', 'biscoito', 'bolacha', 'sorvete', 'mexirica',
            'gatos', 'cachorros', 'passaros', 'peixe', 'avestruz')

for i in palavras:
    print(f'\n"{i.capitalize()}" possui: ', end='')
    for j in i:
        if j in 'aeiou':
            print(j, end=' ')
