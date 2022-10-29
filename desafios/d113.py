def leiaInt(msg):
    n = 0
    try:
        n = int(msg)
    except (ValueError, TypeError):
        print('\033[0;31mERRO: por favor digite um número válido.\033[m')
        n = leiaInt(input('Digite um número inteiro: '))
    except KeyboardInterrupt:
        print('\033[0;31mERRO: por favor digite um número válido.\033[m')
        n = leiaInt(input('Digite um número real: '))
    return n


def leiaFloat(msg): 
    n = 0
    try:
        n = float(msg)
    except (ValueError, TypeError):
        print('\033[0;31mERRO: por favor digite um número válido.\033[m')
        n = leiaFloat(input('Digite um número inteiro: '))
    except KeyboardInterrupt:
        print('\033[0;31mERRO: por favor digite um número válido.\033[m')
        n = leiaFloat(input('Digite um número real: '))
    return n


i = leiaInt(input('Digite um número inteiro: '))
f = leiaFloat(input('Digite um número real: '))

print(f'O valor inteiro digitado foi {i} e o real foi {f:.2f}.')
