from random import randint

comp = randint(1, 10)
palppite = 0
cont = 0
while palppite != comp:
    palppite = int(input('Qual número [1 a 10] o computador "pensou": '))
    if palppite != comp:
        print('Errou! tente de novo.')
    cont += 1
print('\nVocê acertou! Foram necessário(s) {} palpites'.format(cont))