from random import randint
from time import sleep


def sorteia(numeros = []):
    print('Sorteando cinco valores da lista: ', end='')
    for i in range(5):
        numeros.append(randint(1, 100))
        sleep(1)
        print(numeros[i], end=' ')
    print('Pronto!')


def somaPar(numeros = []):
    soma = 0
    print(f'Somando os valores pares de {numeros}, ', end='')
    for i in range(len(numeros)):
        if numeros[i] % 2 == 0:
            soma += numeros[i]
    print(f'temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
