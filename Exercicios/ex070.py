print('-'*30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-'*30)
total = totMil = cont = menor = 0
barato = ''
while True:
    prodNome = str(input('Nome do produto: '))
    prodPreco = float(input('Preço do produto: R$'))
    total += prodPreco
    cont += 1
    if prodPreco > 1000:
        totMil += 1
    if cont == 1 or prodPreco < menor:
        menor = prodPreco
        barato = prodNome

    opcao = ' '
    while opcao not in 'SN':
        print('*' * 30)
        opcao = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
        print('*' * 30)
    if opcao == 'N':
        break
print('{:-^30}'.format('FIM DO PROGRAMA'))
print(f'O total de compras foi R${total:.2f}')
print(f'Temos {totMil} custando mais de mil reias')
print(f'O produto mais barato foi {barato} que custa R${menor}')