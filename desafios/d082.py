valores = list()
pares = list()
impares = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
for i in valores:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'Lista com os valores: {valores}')
print(f'Lista dos valores pares: {pares}')
print(f'Lista dos valores impares: {impares}')