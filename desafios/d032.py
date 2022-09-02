ano = int(input('Digite um ano [ex: 2000, 2013]: '))
if ano % 4 == 0: #etapa 1
    if ano % 100 == 0: #etapa 2
        if ano % 400 == 0: #etapa 3
            print('Ano bissexto') #etapa 4
        else:
            print('Ano não bissexto')  #etapa 5
    else:
        print('Ano bissexto') #etapa 5
else:
    print('Ano não bissexto') #etapa 5
