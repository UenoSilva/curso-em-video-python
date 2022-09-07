valor = int(input('Digite um número: '))
print('O número {} vai ser convertidao para qual base númerica'.format(valor))
print(' 1 - binário')
print(' 2 - octal')
print(' 3 - hexadecimal')
num = int(input('Qual das três opções: '))

if num == 1:
    binario = bin(valor)
    print('{} = {}'.format(valor, binario))
elif num == 2:
    octal = oct(valor)
    print('{} = {}'.format(valor, octal))
elif num == 3:
    hexa = hex(valor)
    print('{} = {}'.format(valor, hexa))
else:
    print('Opção incorreta')

