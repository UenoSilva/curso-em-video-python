print('-=-'*10)
print('Analisador de Triângulos')
print('-=-'*10)
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos PODEM FORMAM triãngulo')
else:
    print('Os segmentos NÃO PODEM triângulo')