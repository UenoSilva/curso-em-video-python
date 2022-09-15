n = int(input('Digite um número: '))
fatorial = 1
print('Calculado {}! ='.format(n), end='')
while n > 0:
    print(' {} '.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    fatorial *= n
    n -= 1
print(fatorial)
