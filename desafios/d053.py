frase = str(input('Digite um frase: ')).strip().split(' ')

f = ''
for i in range(0, len(frase)):
    f += frase[i]

lista = []
cont = 1
for i in range(0, len(f)):
    lista.append(f[i:cont])
    cont+=1

novaF = ''
for i in range(len(lista)-1, -1, -1):
    novaF += lista[i]

if f == novaF:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
