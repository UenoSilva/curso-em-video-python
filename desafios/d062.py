print('-='*20);print('       Progressão Aritmetica')
print('*='*20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 0 #contagem das repetições
rep = 10 #número de repetições
lista = []
while rep != 0:
    print('{}'.format(p), end=' ')
    p += r
    lista.append(p)
    cont+=1
    if cont == rep:
        print('\n')
        rep = int(input('Quantos termos que a mais: '))
        cont = 0
print(lista)
