num = str(input('Digite um número de 0 a 9999: '))
n1 = num[:1]
n2 = num[1:2]
n3 = num[2:3]
n4 = num[3:]

print('unidade: {}'.format(n1))
print('dezena: {}'.format(n2))
print('centena: {}'.format(n3))
print('milhar: {}'.format(n4))
