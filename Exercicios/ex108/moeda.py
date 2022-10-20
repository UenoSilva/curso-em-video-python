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
