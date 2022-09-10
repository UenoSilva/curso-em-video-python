soma = 0
for i in range(1, 500+1):
    if i % 2 == 1:
        if i % 3 == 0:
            soma += i
print('O somatório foi de {}'.format(soma))
