maior = 0
menor = 0
media = 0
soma = 0
cont = 0
frag = 'y'

while frag != 'N' and frag != 'n':
    num1 = int(input('Digite um número: '))
    soma += num1
    cont+=1
    if cont == 1:
        maior = num1
        menor = num1
    else:
        if num1 > maior:
            maior = num1
        if num1 < menor:
            menor = num1
    frag = str(input('Continuar? [y/n]: '))
media = soma / cont

print('Méida dos valores inseridas é {}'.format(media))
print('Maior valor: {}'.format(maior))
print('Menor valor: {}'.format(menor))

