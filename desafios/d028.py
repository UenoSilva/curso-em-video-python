from random import randint

palpite = int(input('Digite um número de 0 a 5: '))
numGerado = randint(0, 5)

if numGerado == palpite:
    print('Você acertou! PARABÉNS')
else:
    print('Você errou!')
    print('Era o número {}! TENTE DE NOVO!'.format(numGerado))
