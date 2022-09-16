print('{:=^40}'.format(' TABUADA 3.0 '))
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*40)
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
    print('-' * 40)
print('{:=^40}'.format(' FIM DA TABUADA 3.0 '))