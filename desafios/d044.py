valorProduto = float(input('Valor do produto: R$'))
print('Condição de pagamemto\n'
      ' 1 - À vista/cheque: 10% de desconto\n'
      ' 2 - À vista no cartão: 5% de desconto\n'
      ' 3 - 2x no cartão: preço normal\n'
      ' 4 - 3x ou mais no cartão: 20% de juros\n')
condPag = int(input('Escolhar uma opção: '))
if condPag == 1:
    print('Valor: {}'.format(valorProduto*(1-10/100)))
elif condPag == 2:
    print('valor: {}'.format(valorProduto*(1-5/100)))
elif condPag == 3:
    print('valor: {}'.format(valorProduto))
elif condPag == 4:
    print('valor: {}'.format(valorProduto*(1+20/100)))
else:
    print('Opção incorreta!')