def validaMoeda(n=0):
    """
    -> Função para verificar se o input está em valor monetário, caso negativo ficará em looping até ser escrito na
    forma correta.
    :param n: input do valor :return: confirmado que está em valor monetário
    """
    while True:
        if ',' in n:
            n = n.replace(',', '.')
        try:
            float(n)
            return float(n)
        except ValueError:
            if not n.isnumeric() or float(n) is False:
                n = input(f'"{n}" não é válido. Digite apenas valores monetários: R$ ').strip()
            else:
                return float(n)
