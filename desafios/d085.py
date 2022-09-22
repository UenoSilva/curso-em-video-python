num = list()
pares = list()
impares = list()

for i in range(0, 7):
    n = int(input(f'Digite o {i+1}º valor: '))
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
num.append(pares[:])
num.append(impares[:])
num[0].sort()
num[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valore impares digitados foram: {num[1]}')
