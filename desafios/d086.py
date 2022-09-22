matriz = []

for i in range(3):
    linha = []
    for k in range(3):
        list.append(linha, 0)
    matriz = matriz + [linha]

for i in range(3):
    for k in range(3):
        matriz[i][k] = int(input('Digite um número: '))
print('-='*30)
for i in range(3):
    for k in range(3):
        print(f'[ {matriz[i][k]} ]', end=' ')
    print('')

