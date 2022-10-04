from time import sleep

def contador(ini, fim, passo):
    if passo > 0:
        if ini > fim:
            passo *= -1
    if passo == 0:
        passo = 1
    for i in range(ini, fim, passo):
        sleep(1)
        print(f'{i} ', end='')
    print('Fim')


print('-='*30)
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 0)
print('-='*30)
print('Contagem de 10 a 0 de 2 em 2')
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
print('-='*30)
print(f'Contagem de {ini} até o {fim} de {pas} em {pas}')
contador(ini, fim, pas)
