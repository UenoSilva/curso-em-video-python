distancia = float(input('Qual é a distância da viagem: '))
if distancia <= 200:
    print('Preço: R${:.2f}'.format(distancia * 0.50))
else:
    print('Preço: R${:.2f}'.format(distancia * 0.45))
