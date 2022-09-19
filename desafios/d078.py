valores = list()
menor = posMaior = maior = posMenor = 0
for c, i in enumerate(range(0, 5)):
    valores.append(int(input(f'Digite um valor na posicao {c}: ')))
    if i == 0:
        maior = menor = valores[i]
        posMaior = posMenor = c
    else:
        if valores[i] > maior:
            maior = valores[i]
            posMaior = c
        if valores[i] < menor:
            menor = valores[i]
            posMenor = c
print('=*'*20)
print(f'Lista de valores: {valores}')
print(f'O maior valor foi {maior} na posicao ', end='')
for n, i in enumerate(valores):
    if i == maior:
        print(f'{n}... ', end='')
print(f'\nO menor valor foi {menor} na posicao ', end='')
for k, i in enumerate(valores):
    if i == menor:
        print(f'{k}... ', end='')
