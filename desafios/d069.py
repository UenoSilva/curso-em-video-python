print('=======Fim do programa========')

contIdade = contHomens = contMulheres = 0
opcao = sexo = ''

while True:
    print('-'*30)
    print('CADRASTRE UMA PESSOA'.center(30))
    print('-' * 30)
    idade = int(input('Idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while opcao != 'S' and opcao != 'N':
        print('-'*30)
        opcao = str(input('Que continuar? [S/N] ')).strip().upper()[0]
        print('-' * 30)
    if opcao in 'N':
        break
    if idade > 18:
        contIdade += 1
    if sexo == 'M':
        contHomens += 1
    if sexo == 'F' and idade < 20:
        contMulheres += 1
    sexo = ''
    opcao = ''
print(f'{contIdade} pessoas acima de 18 foram cadastradas')
print(f'{contHomens} homens foram cadastrados')
print(f'{contMulheres} mulheres abaixo de 20 foram cadastradas')