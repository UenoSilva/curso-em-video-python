from random import randint
from time import sleep

print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
n = int(input('Quantos você quer que eu sorteie? '))

print('-='*4, end=' ')
print(f'{"SORTEANDO OS JOGOS":^10}', end=' ')
print('-='*4)

jogo = list()
numeros = list()
for i in range(n):
    for k in range(6):
        while True:
            if k == 0:
                n = randint(1, 60)
                break
            else:
                n = randint(1, 60)
                if numeros.count(n) > 1:
                    n = randint(1, 60)
                else:
                    break
        numeros.append(n)
    jogo.append(numeros[:])
    numeros.clear()

for pos, i in enumerate(jogo):
    i.sort()
    sleep(3)
    print(f'Jogo {pos+1}: {i}')


print('-='*4, end=' ')
print(f'{"< BOA SORTE! >":^10}', end=' ')
print('-='*4)

