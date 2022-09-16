from random import randint
a1 = randint(1, 10)
a2 = randint(1, 10)
a3 = randint(1, 10)
a4 = randint(1, 10)
a5 = randint(1, 10)
numeros = (a1, a2, a3, a4, a5)

maior = 0
menor = 0
for i in range(0, len(numeros)):
    if i == 0:
        maior = numeros[0]
        menor = numeros[0]
    else:
        if numeros[i] > maior:
            maior = numeros[i]
        if numeros[i] < menor:
            menor = numeros[i]
print('Os números sorteados foram: ', end='')
for i in range(0, len(numeros)):
    print(f'{numeros[i]}', end=' ')
print(f'\nMaior número sorteado foi {maior}')
print(f'Menor número sorteado foi {menor}')

