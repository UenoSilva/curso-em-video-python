aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7.0:
    aluno['Situacao'] = 'Aprovado'
elif 5.0 <= aluno['media'] < 7.0:
    aluno['Situacao'] = 'Recuperação'
else:
    aluno['Situacao'] = 'Reprovado'

for v, a in aluno.items():
    print(f'{v} é igual a {a}')
