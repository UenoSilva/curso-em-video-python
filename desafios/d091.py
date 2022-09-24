from random import randint
from time import sleep
jogador = {'jogador_1': randint(1, 6),
           'jogador_2': randint(1, 6),
           'jogador_3': randint(1, 6),
           'jogador_4': randint(1, 6)}
print('Valores sorteados:')
for v, j in jogador.items():
    print(f'    O {v} tirou {j}')
    sleep(1)
print('Ranking dos jogadores:')
cont = 1
for item in sorted(jogador, key=jogador.get, reverse=True):
    print(f'    {cont}º lugar {item} com {jogador[item]}')
    cont += 1