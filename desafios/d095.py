jogador = dict()
jogadores = list()
gols = list()
soma = 0
while True:
    print('-'*30)
    jogador['nome'] = str(input('Nome do jogador: '))
    num_part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    if num_part > 0:
        for i in range(0, num_part):
            gols.append(int(input(f'Quantos gols na partida {i}? ')))
            soma += gols[i]
        jogador['gols'] = gols[:]
        jogador['total'] = soma
        jogadores.append(jogador.copy())
        gols.clear()
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-'*30)
print(f'{"Cod":<4}{"nome":<10}{"gols":<10}{"total":<6}')
for i in range(0, len(jogadores)):
    print(f'{i:<4}{jogadores[i]["nome"]:<10}{jogadores[i]["gols"]}{jogadores[i]["total"]:>6}')
print('-'*30)
while True:
    n = int(input('Mostrar dados de qual jogador? '))
    if 0 <= n < len(jogadores):
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[n]["nome"]}')
        for i in range(0, len(jogadores[n]['gols'])):
            print(f'    No jogo {i} fez {jogadores[n]["gols"][i]} gols')
    elif n == 999:
        break
    else:
        print(f'ERRO! Não existe jogador com código {n}! Tente Novamente')
print('<< VOLTE SEMPRE >>')
