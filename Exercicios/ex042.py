l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos PODEM FORMAM um triângulo! ', end='')
    if l1 == l2 == l3:
        print('Equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Isóceles')
    elif l1 != l2 != l3:
        print('Escaleno')
else:
    print('Os segmentos NÃO PODEM triângulo')