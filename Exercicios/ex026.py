frase = str(input('Digite uma frase: ')).strip()
print('A letra "A" aparece {} vezes na frase.'.format(frase.upper().count('A')))
print('A primeira letra "A" aparece na posição {}'.format(frase.upper().find('A')))
print('A última letra "A" aparece na posição {}'.format(frase.upper().rfind("A")))
