valores = list()
maior = menor = 0
for i in range(0, 5):
    valores.append(int(input(f'Digite um valor na posicao {i}: ')))
    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]
print('-='*20)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c, i in enumerate(valores):
    if i == maior:
        print(f'{c}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for c, i in enumerate(valores):
    if i == menor:
        print(f'{c}... ', end='')
