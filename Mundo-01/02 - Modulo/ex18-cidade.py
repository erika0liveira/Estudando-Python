cidade = str(input('Digite o nome da cidade: ')).strip()

if cidade.upper().split()[0] == 'SANTO':
    print('O nome da cidade começa com "Santo"')
else:
    print('O nome da cidade não começa com "Santo"')