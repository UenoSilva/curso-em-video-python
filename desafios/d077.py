palavras = ('notebook', 'aprender', 'copo',
            'celular', 'java', 'dormir',
            'cama', 'descansado', 'pronto',
            'vamos', 'estudar')
cont = 0
for i in range(0, len(palavras)):
    var = palavras[i]
    print(f'Na palavra {palavras[i].upper()} temos ', end='')
    for k in range(0, len(var)):
        if var[cont:cont+1] in 'aeiouAEIOU':
            print(f'{var[cont:cont+1]}', end= ' ')
        cont += 1
    print('')
    cont = 0
