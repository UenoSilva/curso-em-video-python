numeros = ('zero', 'um', 'dois', 'três', 'quatro',
          'cinco', 'sis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'quartoze',
          'quinze', 'dezesseis', 'dezessete', 'dezoito',
          'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {numeros[num]}')
