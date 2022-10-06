def fatorial(num=0, show=False):
    """
    -> Calcula o fatorial de um número qualquer inteiro.
    :param num: Número a ser calculado
    :param show: (opcional) Mostrar ou não a solução.
    :return: O valor do fatorial de um número n.
    """
    print('-'*30)
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            if i > 1:
                print(f' {i} x', end='')
            else:
                print(f' {i} =', end='')
    print(f' {f}')
    return f


fatorial(5, True)
