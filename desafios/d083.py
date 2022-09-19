carac = list()

exp = str(input('Digite a expressão: '))

for i in range(0, len(exp)):
    carac.append(exp[i:i+1])

if carac.count('(') == carac.count(')'):
    print('Expressão válida!')
else:
    print('Expressão inválida!')

