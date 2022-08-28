sal = float(input('Qual é o salário do funcionário? R$'))
novoSal = sal * ((100+15)/100)
print('Um funcionário que ganhava R${:.2f}, agora com o reajuste de 15% vai ganhar R${:2.f}'.format(sal, novoSal))
