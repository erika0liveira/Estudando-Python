def notas(*num, sit=False):
    """
    -> Função para calcular a média de alunos e a situação da classe
    :param num: aceitar várias notas
    :param sit: opcional para mostrar a situação da classe
    :return: dicionário com os resultados
    """
    nts = {'total': len(num),
           'maior': max(num),
           'menor': min(num),
           'media': sum(num) / len(num)}
    if sit:
        if nts['media'] < 6:
            nts['situação'] = 'ruim'
        elif 8 > nts['media'] >= 6:
            nts['situação'] = 'razoável'
        else:
            nts['situação'] = 'boa'
    return nts


n = notas(5.5, 2.5, 1.5, sit=True)
print(f'\n{n}\n')

help(notas)
