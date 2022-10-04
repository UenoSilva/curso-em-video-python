
def calcular_terreno(l, c):
    area = l * c
    return area


print('Controle de terreno')
print('='*30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
print(f'A área de um terreno {l:.2f}x{c:.2f} e de {calcular_terreno(l, c):.2f}m²')
