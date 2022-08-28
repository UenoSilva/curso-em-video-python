from math import sin, cos, tan

ang = float(input('Digite o ângulo: '))
seno = sin(ang)
coss = cos(ang)
tang = tan(ang)

print('Seno({0}°) = {1}\nCosseno({0}°) = {2}\nTangente({0}°) = {3}'.format(ang, seno, coss, tang))
