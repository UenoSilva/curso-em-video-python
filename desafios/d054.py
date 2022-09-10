from datetime import date

ano = date.today().year

cont1 = 0
cont2 = 0
for i in range(0, 7):
    anoNasc = int(input('Digite o ano de nascimento da {}° pessoa: '.format(i+1)))
    if ano - anoNasc < 18:
        cont1+=1
    else:
        cont2+=1
print('{} pessoa(s) não atingiram a maioridade!'.format(cont1))
print('{} pessoa(s) já são maiores de idade'.format(cont2))