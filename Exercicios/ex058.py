from random import randint
computador = randint(0, 10)
print('Sou seu computador...\n'
      'Acabei de pensar num número de 0 a 10\n'
      'Consegue adivinha?')
palpite = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Aceetou com {} tentativas. Parabéns'.format(palpite))