from datetime import date

anoAtual = date.today().year
contMenor = 0
contMaior = 0

for i in range(1, 8):
    ano = int(input('Digite o ano da {}ª pessoa: '.format(i)))
    if (anoAtual - ano) >= 18:
        contMaior += 1
    else:
        contMenor += 1

print('{} pessoas são menores de idade'.format(contMenor))
print('{} pessoas são maiores de idade'.format(contMaior))
