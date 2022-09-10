num = int(input('Digite um número: '))
print('Escolhar uma das bases para convenção:')
print('[ 1 ] - Binário')
print('[ 2 ] - Octal')
print('[ 3 ] - Hexadecimal')
opção = int(input('Sua opção: '))

if opção == 1:
    print('{} converido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igaul a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))