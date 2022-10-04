def area(lar, com):
    a = lar * com
    print(f'A área de um terreno {lar}x{com} é de {a}m²')


print(f'{"Controle de Terreno":^25}')
print('-'*25)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
