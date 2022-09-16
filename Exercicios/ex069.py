print('-'*30)
print('{:^30}'.format('CADRASTRO DE PESSOAS'))
print('-'*30)
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar: [S/N}')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'\nTotal de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadrastrados')
print(f'Ao todo temos {totM20} mulheres com menos de 20 anos')