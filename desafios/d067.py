while True:
    n = int(input('Ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*30)
    for i in range(1, 11):
        print(f'{n:2} x {i:2} = {i*n:2}')
    print('-'*30)
print('Tabuada encerrada!')