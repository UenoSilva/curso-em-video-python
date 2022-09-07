idade = int(input('Informe sua idade: '))

if idade < 18:
    print('Ainda vai se alistar ao serviço militar')
    print('Falta {} anos até o alistamento'.format(18-idade))
elif idade == 18:
    print('É hora de alista-se no serviço militar')
else:
    print('Já passou do tempo de alistamento')
    print('Passou {} anos do alistamento'.format(idade-18))
