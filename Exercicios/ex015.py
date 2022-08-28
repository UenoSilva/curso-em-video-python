km = float(input('Quantos Km o carro andou: '))
dias = int(input('Quantos dias o carro foi alugado: '))
preco = (km*0.15)+(dias*60)
print('O total a pagar é de R${:.2f}'.format(preco))