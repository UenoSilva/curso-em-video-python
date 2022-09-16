listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estoko', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

print('-'*40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-'*40)
for i in range(0, len(listagem)):
    if i % 2 == 0:
        print('{:.<31}'.format(listagem[i]), end='')
    else:
        print('R$ {:>6.2f}'.format(listagem[i]))
print('-'*40)
