salario = float(input('Qual é salário do funcionário: '))
newSalario = 0
if salario > 1250.0:
    newSalario = salario * (1 + 10/100)
else:
    newSalario = salario * (1 + 15/100)

print('Novo salário de R${:.2f}'.format(newSalario))
