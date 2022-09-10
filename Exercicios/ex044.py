print('='*10, 'LOJAS UENO', '='*10)
compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
 [1] - À vista dinheiro/cheque: 10% de desconto
 [2] - À vista no cartão: 5% de desconto
 [3] - 2x no cartão: preço normal
 [4] - 3x ou mais no cartão: 20% de juros''')
opcao = int(input('Qual é a opção: '))

if opcao == 1:
    total = compras * (1 - 10/100)
elif opcao == 2:
    total = compras * (1 - 5/100)
elif opcao == 3:
    total = compras
    parcela = total/2
    print('Sua comprar foi parcelado em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = compras * (1 + 20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total/totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = compras
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamento')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compras, total))
