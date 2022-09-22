pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append((int(input('Peso: '))))
    pessoas.append(dados[:])
    dados.clear()
    print('-'*20)
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break

for pos, p in enumerate(pessoas):
    if pos == 0:
        maior = menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]
        if p[1] < menor:
            menor = p[1]

print('-'*20)
print(f'Você cadrastrou {len(pessoas)} pessoas!')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for i in pessoas:
    if i[1] == maior:
        print(f'[{i[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for k in pessoas:
    if k[1] == menor:
        print(f'[{k[0]}]', end=' ')
