def par(n=0):
    """
    -> Verificar se n é par ou impar
    :valor n:
    :return: True ou False
    """
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É impar!')