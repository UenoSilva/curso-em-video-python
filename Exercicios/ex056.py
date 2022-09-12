soma = 0
maior = 0
cont = 0
media = 0
nomeVelho = ''
for i in range(1, 5):
    print('---- {}° pessoa ----'.format(i))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    print('--------------------')
    soma += idade
    if i == 1 and sexo in 'Mn':
        maior = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        cont += 1
media = soma / 4
print('\nA média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, nomeVelho))
print('{} mulhres tem menos de 20 anos'.format(cont))
