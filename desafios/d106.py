def msg():
    print('\033[1;30;102m',end='')
    print('~'*30)
    print(f'{"SISTEMA DE AJUDA PyHELP":^30}')
    print('~' * 30)
    print('\033[m', end='')


def msg2():
    print('\033[1;30;101m', end='')
    print('~' * 13)
    print(f'{"ATÉ LOGO!":^13}')
    print('~' * 13)
    print('\033[m', end='')


def men(m):
    mensa = "Acessando o manual do comando " + m
    tam = len(mensa)+4
    print('\033[1;30;106m', end='')
    print('~'*tam)
    print(f'{mensa:^{tam}}')
    print('~'*tam)
    print('\033[m', end='')


def manual(m):
    men(m)
    print(f'\033[1;30;107m', end='')
    help(m)
    print('\033[m', end='')


while True:
    msg()
    r = str(input('Função ou Biblioteca > '))
    if r == 'fim':
        break
    else:
        manual(r)
msg2()
