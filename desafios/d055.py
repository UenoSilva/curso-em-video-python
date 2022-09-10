menor = 9999
maior = 0
for i in range(0, 5):
    peso = int(input('Peso: '))
    if peso >= maior:
        maior = peso
    if peso <= menor:
        menor = peso

print('Maior peso: {}'.format(maior))
print('Menor peso: {}'.format(menor))


