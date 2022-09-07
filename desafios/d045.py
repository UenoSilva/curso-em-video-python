import random

lista = ['pedra', 'papel', 'tesoura']
jogador = int(input('Escolhar uma das opções abaixo:\n'
                    ' 1 - pedra\n'
                    ' 2 - papel\n'
                    ' 3 - tesoura\n'
                    'Esclhar: '))
computador = random.randint(1, 3)

print('Jogaor escolheu {}'.format(lista[jogador-1]))
print('Computador escolheu {}'.format(lista[computador-1]))

if jogador==computador:
    print('Empate')
elif jogador==1 and computador==2:
    print('Computador ganhou')
elif jogador==1 and computador==3:
    print('Jogador ganhou')
elif jogador==2 and computador==3:
    print('Computador ganhou')
elif jogador==2 and computador==1:
    print('Jogador ganhou')
elif jogador==3 and computador==1:
    print('Computador ganhou')
elif jogador==3 and computador==2:
    print('Jogador ganhou')
