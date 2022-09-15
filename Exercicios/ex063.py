print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
cont = 3
print('{} -> {}'.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(' -> {}'.format(t3), end='')
    cont += 1
print(' -> FIM')
print('~'*30)
