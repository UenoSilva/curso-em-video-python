vel = float(input('Velocidade do carra: '))
if vel > 80.0:
    print('Velocidade ultrapassada!')
    print('Você foi multado em: R${:.2f}'.format((vel - 80.0) * 7.0))
else:
    print('Velocidade nos conformes')
