def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: o número a ser calculado
    :param show: (opcional) mostrar a solução
    :return: retorna o resultado
    """
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(f'{i}', end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f


print(fatorial(6, False))
