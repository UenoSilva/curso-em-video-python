prod = float(input('Qual é o preço do produto? R$'))
prodDesc = prod * ((100-5)/100)
print('O produto que custava R${:.2f}, agora custa na promoção com descconto de 5% vai custa R${:.2f}'.format(prod, prodDesc))

