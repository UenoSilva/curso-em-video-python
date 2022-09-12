s = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
        cont += 1
print('A soma dos {} valores é {}'.format(cont, s))
