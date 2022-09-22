matriz = []
for i in range(3):
    linha = []
    for k in range(3):
        list.append(linha, 0)
    matriz = matriz + [linha]

for i in range(3):
    for k in range(3):
        matriz[i][k] = int(input(f'Digite um valor para [{i},{k}]: '))

print('-='*30)
for i in range(3):
    for k in range(3):
        print(f'[ {matriz[i][k]} ]', end=' ')
    print('')
print('-='*30)
soma = 0
for i in range(3):
    for k in range(3):
        if matriz[i][k] % 2 == 0:
            soma += matriz[i][k]
print(f'A soma dos valores pares é {soma}')

somaTC = 0
for i in range(3):
    somaTC += matriz[i][2]
print(f'A soma dos valores da terceira coluna é {somaTC}')

maior = 0
for i in range(3):
    if matriz[1][i] > maior:
        maior = matriz[1][i]
print(f'O maior valor da segunda linha é {maior}')
