ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',
       'vinte e um', 'vinte e dois', 'vinte e três', 'vinte e quatro', 'vinte e cinco', 'vinte e seis',
       'vinte e sete', 'vinte e oito', 'vinte e nove', 'trinta', 'trinta e um', 'trinta e dois', 'trinta e três',
       'trinta e quatro', 'trinta e cinco', 'trinta e seis', 'trinta e sete', 'trinta e oito', 'trinta e nove',
       'quarenta', 'quarenta e um', 'quarenta e dois', 'quarenta e três', 'quarenta e quatro', 'quarenta e cinco',
       'quarenta e seis', 'quarenta e sete', 'quarenta e oito', 'quarenta e nove', 'cinquenta')

n = None

while True:
    if n is None:
        n = input('\nDigite um número entre 0 e 50: ')
    if n.isdigit() is False or int(n) < 0 or int(n) > 50:
        n = input('Por favor, apenas números entre 0 e 50: ')
    elif n.isdigit() is True:
        n = int(n)
        print(ext[n].capitalize())
        n = input('\nQuer ler mais um número? Sim = número / Não = X: ').upper()
        if n == 'X':
            print('\nPrograma encerrado.')
            break
