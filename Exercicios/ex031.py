dist = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}KM'.format(dist))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.40

print('É o preço da sua passagem será de R${:.2f}'.format(preco))
