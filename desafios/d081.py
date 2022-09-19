valores = list()
cont = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    cont += 1
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print('=-'*20)
print(f'Foram digitado {cont} números')
valores.sort(reverse=True)
print(f'Lista em ordem decrescente: {valores}')
if valores.count(5) > 0:
    print(f'O número 5 está na lista')
else:
    print('O número 5 não está na lista')
