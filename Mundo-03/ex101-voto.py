def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f'Com {idade}, o voto ', end='')
    if idade < 18:
        return 'NÃO É OBRIGÁTÓRIO.'
    elif 18 < idade < 70:
        return 'É OBRIGATÓRIO.'
    elif idade > 70:
        return 'É FACULTATIVO.'


print(f'{voto(ano=int(input("Digite o ano do seu nascimento: ")))}')
