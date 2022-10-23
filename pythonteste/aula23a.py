def dividir():
    a = int(input('Numerador: '))
    b = int(input('Demominador: '))
    r = a / b
    return r


try:
    r = dividir()
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário não informou os dados')
else:
    print(f'O resultado é {r}')
finally:
    print('volte sempre. muito obrigado')