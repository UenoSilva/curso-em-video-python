p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dec = p + (10 - 1) * r
for i in range(p, dec+r, r):
    print(i, end=' ')
