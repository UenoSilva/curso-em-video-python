dados = dict()
pessoas = list()
soma = media = 0
while True:
    dados.clear()
    print('-='*30)
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [F/M]: ')).strip().upper()[0]
        if dados['sexo'] in 'FM':
            break
        print('Error! Tente novamente.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    opcao = str(input('Quer continuar? [S?N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-='*30)
print(pessoas)
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma / len(pessoas)
print(f'A média das idades é de {media:.2f} anos')
print(f'As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'A lista de pessoas que estão acima da média: ', end='')
for i in pessoas:
    if i['idade'] >= media:
        print()
        for k, i in i.items():
            print(f'{k} = {i} ', end='')
        print()
print('<< ENCERADO >>')
