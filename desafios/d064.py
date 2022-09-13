num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input('Digite um número ou 999 para sair:'))
    if num != 999:
        soma += num
        cont += 1
print('\nForam digitados {} números\n'
      'e a soma deles foi de {}'.format(cont, soma))
