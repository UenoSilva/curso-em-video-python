aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Méida de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')