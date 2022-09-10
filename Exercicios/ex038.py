num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('{} é maior\n{} é o menor'.format(num1, num2))
elif num2 > num1:
    print('{} é o maior\n{} é o menor'.format(num2, num1))
else:
    print('Os dois valores são iguais')
