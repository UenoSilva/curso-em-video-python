from time import sleep


def contador(ini, fim, pas):
    if pas < 0:
        pas *= -1
    if pas == 0:
        pas = 1
    print('-='*20)
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}')

    if ini < fim:
        cont = ini
        while cont <= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += pas
        print('Fim!')
    else:
        cont = ini
        while cont >= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= pas
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
