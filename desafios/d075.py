
v1 = int(input('Diigite um número: '))
v2 = int(input('Diigite um número: '))
v3 = int(input('Diigite um número: '))
v4 = int(input('Diigite um número: '))
num = (v1, v2, v3, v4)
cont9 = 0
posi = 0
pares = 0
for p, i in enumerate(num):
    if i == 9:
        cont9 += 1
    if i == 3:
        posi = p+1
    if i % 2 == 0:
        pares += 1
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {cont9} vezes')
print(f'O valor 3 apareceu na {posi}ª posição')
print(f'Os valores pares digitados foram {pares}')

