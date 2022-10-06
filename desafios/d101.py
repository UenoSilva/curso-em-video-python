from datetime import date


def voto(ano_nasc=0):
    ano = date.today().year
    idade = ano - ano_nasc
    if idade < 18:
        return 'NEGADO'
    elif 18 < idade < 70:
        return 'OBRIGATÓRIO'
    else:
        return 'OPCIONAL'


ano_nasc = int(input('Em que ano você nasceu? '))
print(f'Com {date.today().year - ano_nasc} anos: VOTO {voto(ano_nasc)}')