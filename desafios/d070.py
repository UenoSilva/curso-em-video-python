print('-'*40)
print('LOJA SUPER BARATÃO'.center(40))
print('-'*40)
opcao = ''
soma = contProd = 0
menorValorProd = ''
m = 999
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    soma += preco
    if preco > 1000:
        contProd += 1
    if preco < m:
        m = preco
        menorValorProd = nome
    opcao = ''
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Continuar: [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
print('{:-^40}'.format('Fim do Programa'))
print(f'Total gasto R${soma}')
print(f'{contProd} produto(s) custam mais de R$1000,00')
print(f'O produto mais barato é o {menorValorProd}')