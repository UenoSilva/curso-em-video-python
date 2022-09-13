num = int(input('Digite um valor: '))
cont = 0
aux = 1
aux1 = 0
print('0 {}'.format(aux), end=' ')
while cont < num:
    fibo = aux + aux1
    aux1 = aux
    aux = fibo
    print(fibo, end=' ')
    cont+=1

