def metade(n=0, formata=True):
    """
    -> Função para calcular a metade de um valor.
    :param n: valor a ser dividido
    :param formata: opcional para retornar o valor formatado em real (R$)
    :return: resultado do dobro
    :return:
    """
    res = n / 2
    return res if not formata else moeda(res)


def dobro(n=0, formata=True):
    """
    -> Função para calcular o dobro de um valor.
    :param n: valor a ser duplicado
    :param formata: opcional para retornar o valor formatado em real (R$)
    :return: resultado
    """
    res = n * 2
    return res if not formata else moeda(res)


def aumentar(v=0, aum=0, formata=True):
    """
    -> Função para aumentar um valor de acordo com uma porcentagem
    :param v: valor para base de cálculo
    :param aum: porcentagem de aumento
    :param formata: opcional para retornar o valor formatado em real (R$)
    :return: resultado
    """
    res = v + (v * (aum / 100))
    return res if not formata else moeda(res)


def diminuir(v=0, dim=0, formata=True):
    """
    -> Função para diminuir um valor de acordo com uma porcentagem
    :param v: valor para base de cálculo
    :param dim: porcentagem de redução
    :param formata: opcional para retornar o valor formatado em real (R$)
    :return: resultado
    """
    res = v - (v * (dim / 100))
    return res if not formata else moeda(res)


def moeda(n=0):
    """
    -> Função para retornar o valor formatado em real (R$)
    :param n: Valor a ser formatado
    :return:
    """
    return f'R$ {n:.2f}'


def resumo(v=0, aum=0, dim=0):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(v)}')
    print(f'Metade do preço: \t{metade(v)}')
    print(f'Dobro do preço: \t{dobro(v)}')
    print(f'{aum} % de aumento: \t{aumentar(v, aum)}')
    print(f'{dim} % de redução: \t{diminuir(v, dim)}')
    print('-' * 30)
