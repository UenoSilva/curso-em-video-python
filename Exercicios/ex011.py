alt = float(input('Altura da parede: '))
lar = float(input('Largura da parede: '))
area = alt*lar

print('Sua parede tem a dimensão de {}x{} e sua área e de {}'.format(lar, alt, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(area/2))
