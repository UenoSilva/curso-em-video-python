alunos = list()
nomes = list()
notas = list()

while True:
    print('-'*50)
    nome = str(input('Nome: '))
    nomes.append(nome)
    n1 = float(input('Nota 1: '))
    notas.append(n1)
    n2 = float(input('Nota 2: '))
    notas.append(n2)
    print('-' * 50)
    alunos.append(nomes[:])
    alunos.append(notas[:])
    nomes.clear()
    notas.clear()
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break

print('-='*25)
print('No. Nome       Média')
print('-'*50)
cont = 0
for i in range(0, len(alunos)):
    if i % 2 == 0:
        print(f'{cont}', end='   ')
        for n in alunos[i]:
            print(f'{n}', end=' ')
        cont += 1
    else:
        soma = 0
        for k in alunos[i]:
            soma += k
        print(f'{soma:>10}')

op = 0
while op != 999:
    print('-'*50)
    op = int(input('Mostrar notas de qual aluno? (999 interrompw): '))
    if op == 999:
        break
    for i in alunos[op+op]:
        print(f'Notas de {i} são {alunos[op+op+1]}')
