valores = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    if valores.count(valores[len(valores)-1]) > 1:
        valores.pop()
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print('-='*20)
print(f'{valores.sort()}') 
