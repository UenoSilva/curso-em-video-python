opcao = 0
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

while opcao != 5:
    print('--------- Menu --------\n'
          ' [1] somar             \n'
          ' [2] multiplicar       \n'
          ' [3] maior             \n'
          ' [4] novos número      \n'
          ' [5] sair do programa  ')
    opcao = int(input('Sua opção: '))

    if opcao == 1:
        soma = num1 + num2
        print('Somar: {} + {} = {}'.format(num1, num2, soma))
    elif opcao == 2:
        multiplicar = num1 * num2
        print('Multiplicar: {} * {} = {}'.format(num1, num2, multiplicar))
    elif opcao == 3:
        if num1 > num2:
            print('Maior: {}'.format(num1))
        else:
            print('Maior: {}'.format(num2))
    elif opcao == 4:
        num1 = int(input('Digite um novo número: '))
        num2 = int(input('Digite um novo número: '))
    elif opcao == 5:
        opcao = 5
        print('Fechando programa')
    else:
        print('Opção Inválida!!!')