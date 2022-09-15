from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*20)
res = ''
cont = 0
while True:
    valor = int(input('Diga um valor: '))
    escolhar = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    computador = randint(0, 9)
    soma = computador + valor
    if soma % 2 == 0:
       res = 'PAR'
    else:
        res = 'IMPAR'
    print('-'*20)
    print(f'Você jogou {valor} e o computador {computador}. Total de {soma} DEU {res}')
    print('-' * 20)
    if res == 'PAR':
        if escolhar == 'P':
            cont += 1
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('=-'*20)
        if escolhar == 'I':
            print('Você PERDEU')
            break
    elif res == 'IMPAR':
        if escolhar == 'I':
            cont += 1
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('=-' * 20)
        if escolhar == 'P':
            print('Você PERDEU')
            break
print(f'Game Over! Você venceu {cont} vez(es)')
