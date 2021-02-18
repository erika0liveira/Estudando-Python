frase = str(input('Digite uma frase: ')).upper()

#tirar os espaços da frase input
frase2 = frase.replace(' ', '')

#Invertendo a frase já sem espaços
freverso = frase2[len(frase2)::-1]

if frase2 == freverso:
    print('\nA frase "{}" invertida fica "{}", portanto É um PALÍNDROMO!'.format(frase, freverso))
else:
    print('\nA frase "{}" invertida fica "{}", portanto NÃO é um PALÍNDROMO!'.format(frase, freverso))