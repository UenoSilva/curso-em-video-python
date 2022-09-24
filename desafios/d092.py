from datetime import date
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
anoNasc = int(input('Ano de nascimento: '))
ano = date.today().year
pessoa['idade'] = ano - anoNasc
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] > 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (pessoa['contratação'] - anoNasc) + 35
print('-='*30)
print(pessoa)
for v, i in pessoa.items():
    print(f'{v} tem valor {i}')
