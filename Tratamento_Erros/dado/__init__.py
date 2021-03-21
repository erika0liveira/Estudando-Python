def leint(n=0):
    """
    -> Testa se um número é int, em looping até se inputado um int.
    :param n: input do valor
    :return: resultado do teste.
    """
    while True:
        try:
            int(n)
        except (ValueError, TypeError):
            n = input(f'"{n}" não é um valor inteiro. Digite um número válido: ')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não informar esse valor!')
            return 0
        else:
            return print(f'\nO numero inteiro digitado foi {n}\n')


def lefloat(n=0):
    """
    -> Função para verificar se o input está em valor monetário, caso negativo ficará em looping até ser escrito na
    forma correta.
    :param n: input do valor
    :return: confirmado que está em valor monetário
    """
    while True:
        if ',' in n:
            n = n.replace(',', '.')
        try:
            float(n)
        except KeyboardInterrupt:
            print('O usuário preferiu não informar esse valor!')
            return 0
        except ValueError:
            n = input(f'"{n}" não é válido. Digite apenas valores monetários: R$ ').strip()
        else:
            return print(f'\nVocê digitou o número FLOAT {float(n)}\n')


def testaurl(url):
    """
    -> Função para testar se um site está dísponivel.
    :param url: url.
    :return: resultado do teste.
    """
    import requests
    try:
        requests.get(url)
    except requests.exceptions.ConnectionError:
        print('Não foi possível acessar o site Pudim')
    else:
        print('Foi possível acessar o site Pudim')
