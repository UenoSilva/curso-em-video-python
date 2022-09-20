valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    while True:
        opcao = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print('=-'*20)
print(f'Você digitou {len(valores)} tantos valores')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente é {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')