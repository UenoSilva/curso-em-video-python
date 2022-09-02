n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n1 > n2:
    if n1 > n3:
        print('O maior número é {}'.format(n1))
        if n2 > n3:
            print('O menor número é {}'.format(n3))
        else:
            print('O menor número é {}'.format(n2))
    else:
        print('O maior número é {}'.format(n3))
        if n1 > n2:
            print('O menor número é {}'.format(n2))
        else:
            print('O menor número é {}'.format(n1))
else:
    if n2 > n3:
        print('O maior número é {}'.format(n2))
        if n1 > n3:
            print('O menor número é {}'.format(n3))
        else:
            print('O menor número é {}'.format(n1))
    else:
        print('O maior número é {}'.format(n3))
        if n2 > n1:
            print('O menor número é {}'.format(n1))
        else:
            print('O menor número é {}'.format(n2))
