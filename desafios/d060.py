fatorial = 1
num = int(input('Digite um número: '))
aux = num
while num != 0:
    fatorial *= num
    num -= 1
print('{}! = {}'.format(aux, fatorial))
