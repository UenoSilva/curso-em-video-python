cont = soma = 0
while True:
    num = int(input('Diigte um número, 999 para sair: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} números e a soma deles foi de {soma}')
