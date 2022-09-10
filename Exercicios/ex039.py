import datetime
anoNasc = int(input('Ano de nascimento: '))
idade = datetime.date.today().year - anoNasc
print('Quem nasceu em {} tem {} em {}'.format(anoNasc, idade, datetime.date.today().year))
if idade == 18:
    print('Você tem que alista-se IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    alistamento = datetime.date.today().year + saldo
    print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
    print('O seu alistamento será em {}'.format(alistamento))
elif idade > 18:
    saldo = idade - 18
    alistamento = datetime.date.today().year-saldo
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    print('O seu alistamento foi em {}'.format(alistamento))


