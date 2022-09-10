num = int(input('Digite um número: '))
aux = 0
for i in range(2, num-1):
    if num % i == 0:
        aux = 1
if aux == 0:
    print('{} é primo'.format(num))
else:
    print('{} não é primo'.format(num))

