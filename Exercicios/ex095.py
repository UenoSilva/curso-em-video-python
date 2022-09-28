jogadores = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear()
    for c in range(0, tot):
        gols.append(int(input(f'    Quantos gols na partida {c}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-='*30)
while True:
    busca = int(input('MOstrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGODOR {jogadores[busca]["nome"]}')
        for i, g in enumerate(jogadores[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
print('-='*30)
print('<< VOLTE SEMPRE >>')
