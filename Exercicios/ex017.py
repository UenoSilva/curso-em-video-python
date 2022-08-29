from math import sqrt, pow

catOpos = float(input('Comprimento do cateto oposto: '))
catAdja = float(input('Comprimento do cateto adjacente: '))
hipo = sqrt(pow(catAdja, 2)+pow(catOpos, 2))
print('A hipotenusa vai medir {:.2f}'.format(hipo))
