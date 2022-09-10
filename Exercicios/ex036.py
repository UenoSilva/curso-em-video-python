valorCasa = float(input('Valor da casa: R$'))
salarioComp = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
valorPrestacao = valorCasa/(12*anos)
minimo = salarioComp*30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valorCasa, anos))
print(' a prestação será de R${:.2f} e o mínimo será de R${:.2f}'.format(valorPrestacao, minimo))
if valorPrestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')

