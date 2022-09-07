import math

peso = float(input('Qual é o seu peso: '))
altura = float(input('Qual é a sua altura: '))

imc = peso/(math.pow(altura, 2))

if imc < 18.5:
    print('Abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepesp')
elif imc >= 30 and imc < 40:
    print('Obsidade')
else:
    print('Obsidade mórbida')
