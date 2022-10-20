def aumentar(n=0, v=0, formato=False):
    res = n * (1 + v/100)
    return res if formato is False else moeda(res)


def diminuir(n, v, formato=False):
    res = n * (1 - v/100)
    return res if formato is False else moeda(res)


def dobro(n, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def metade(n, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


def resumo(p=0, t_aumento=10, t_reducao=5):
    """
    -> Função que mostrar os dados de um preço
    :param p: preço a ser calculado
    :param t_aumento: variável de aumento do preço
    :param t_reducao: variável de redução do preço
    """
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^{30}}')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Aumento de {t_aumento}%: \t{aumentar(p, t_aumento, True)}')
    print(f'Redução de {t_reducao}%: \t{diminuir(p, t_reducao, True)}')
    print('-'*30)