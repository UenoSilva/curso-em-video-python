jogador = dict()
gols = list()
quant_gols = 0
jogador['nome'] = str(input('Nome do Jogador: '))
n_part = int(input(f'Quantas partidads {jogador["nome"]} jogou? '))
for i in range(0, n_part):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
    quant_gols += gols[i]
jogador['gols'] = gols
jogador['total'] = quant_gols
print('-='*30); print(jogador); print('-='*30)
for v, i in jogador.items():
    print(f'O campo {v} tem valor {i}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {n_part} partidas.')
for i in range(0, n_part):
    print(f'    =>Na partida {i}, fez {gols[i]} gols.')
print(f'Foi um total de {jogador["total"]} gols')
