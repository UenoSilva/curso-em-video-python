numero = ('zero', 'um', 'dois', 'três', 'quatro',
          'cinco', 'sis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'quartoze',
          'quinze', 'dizesseis', 'dizesete', 'dezoito',
          'dezenove', 'vinte')

num = int(input('Digite um número entre 0 e 20: '))
while num < 0 or num > 20:
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numero[num]}')
