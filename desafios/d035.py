from math import fabs

l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

cond1 = False
cond2 = False
cond3 = False

#testa se a primeira condição é verdadeira
if fabs(l2-l3) < l1:
    if l1 < (l2+l3):
        cond1 = True
    else:
        cond1 = False
else:
    cond1 = False
#testa se a segunda condição é verdadeira
if fabs(l1-l3) < l2:
    if l2 < (l1+l3):
        cond2 = True
    else:
        cond2 = False
else:
    cond2 = False
#testa se a terceira condição é verdadeira
if fabs(l1-l2) < l3:
    if l3 < (l1+l2):
        cond3 = True
    else:
        cond3 = False
else:
    cond3 = False

#verificação final das condições
if cond1:
    if cond2:
        if cond3:
            print('Forma um triângulo')
        else:
            print('Não forma')
    else:
        print('Não forma')
else:
    print('Não forma')
