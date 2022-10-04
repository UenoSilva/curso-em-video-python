from random import randint
from time import sleep


def sorteia(numeros):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('Pronto!')


def somaPar(numeros):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {numeros}, temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
