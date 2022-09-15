resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Diigite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [s/n] ')).upper().strip()[0]
media = soma / quant
print('\nVocê digitou {} números e a media foi {}'.format(quant, media))
print('O maior foi {} e o menor foi {}'.format(maior, menor))