valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantoas para quitar a casa: '))

valorPrestacao = valor_casa / anos

if (valorPrestacao*100)/salario > 30:
    print('Negado')
else:
    print('Permitido, valor da prestação: {}'.format(valorPrestacao))
