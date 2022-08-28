from math import sqrt, pow

catOp = float(input('Cateto oposto: '))
catAd = float(input('Cateto adjaebte: '))
hipot = sqrt(pow(catOp, 2) + pow(catAd, 2))
print('A hipotenusa é {}'.format(hipot))
