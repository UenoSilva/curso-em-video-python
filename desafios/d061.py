print('-='*20)
print('       Progressão Aritmetica')
print('*='*20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 1

while cont <= 10:
    print('{}'.format(p), end=' ')
    p+=r
    cont+=1