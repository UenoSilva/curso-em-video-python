from random import randint
from time import sleep
comp = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == comp:
    print('PRABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} é não no {}!'.format(comp, jogador))
