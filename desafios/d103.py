def ficha(nome='<desconhecido>', gols=0):
    return print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do jogador: '))
gols = str(input('Número de Gols: '))
if (nome == '') & (gols == ''):
    ficha()
elif nome == '':
    ficha(gols=gols)
elif gols == '':
    ficha(nome=nome)
else:
    ficha(nome, gols)

