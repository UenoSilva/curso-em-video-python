salario = float(input('Qual é o salário do funcionário: '))
if salario <= 1250:
    novoSalario = salario * (1 + 15/100)
else:
    novoSalario = salario * (1 + 10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novoSalario))
