soma = 0
nomeVelhor = ''
contMulheres = 0
maiorH = 0

for i in range(0, 4):
    print('-'*10)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: '))
    soma+=idade
    print('-' * 10)
    if sexo == 'm' and idade >= maiorH:
        nomeVelhor = nome
        maiorH = idade
    if sexo == 'f' and idade <= 20:
        contMulheres+=1
media = soma/4
print('A média das idades é {}'.format(media))
print('O home mais velhor é {}'.format(nomeVelhor))
print('{} mulheres tem menos de 20 anos'.format(contMulheres))