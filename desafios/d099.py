from time import sleep


def maior(l=[]):
    print('-=' * 25)
    print('Analisando os valores passados....')
    if len(l) == 0:
        print(f'Foram informados {0} valores ao todo.')
        print(f'O maior valor informado foi 0.')
    else:
        for i in l:
            print(f'{i} ', end='')
            sleep(1)
        print(f'Foram informados {len(l)} valores ao todo.')
        print(f'O maior valor informado foi {max(l)}.')


maior(l=[2, 9, 4, 5, 7, 1])
maior(l=[4, 7, 0])
maior(l=[1, 2])
maior(l=[6])
maior(l=[])

