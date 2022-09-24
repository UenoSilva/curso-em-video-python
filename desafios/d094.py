pessoas = list()
dados = dict()
media = soma = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-='*30)
print(f' - O grupo tem {len(pessoas)} pessoas.')
for i in range(0, len(pessoas)):
    soma += pessoas[i]['idade']
media = soma / len(pessoas)
print(f' - A média de idade é de {media:.2f} anos.')
print(' - As mulheres cadrastradas foram: ', end='')
for i in range(0, len(pessoas)):
    if pessoas[i]['sexo'] == 'F':
        print(f'{pessoas[i]["nome"]} ', end='')
print('\n - Lista de pessoas que estão acima da média:')
for i in range(0, len(pessoas)):
    if pessoas[i]['idade'] > media:
        print(f'\n  nome = {pessoas[i]["nome"]}; sexo = {pessoas[i]["sexo"]}; idade = {pessoas[i]["idade"]};')
print('<< Encerado >>')
