
times = ('Palmeiras', 'Internacional', 'Flamengo',
         'Fluminense', 'Corithias', 'Athletico-PR',
         'Atlético-MG', 'América-MG', 'Goiás',
         'Santos', 'Bragantino', 'Botafogo',
         'São Paulo', 'Ceará SC', 'Fortaleza',
         'Coritiba', 'Cuiabá', 'Avaí',
         'Atlético-GO', 'Juventude')

print(f'Cinco primeiros colocados: {times[0:5]}')
print(f'Quatro últimos colocados: {times[16:]}')
print(sorted(times))
posicao = 0
for pos, time in enumerate(times):
    if time == 'Santos':
        posicao = pos + 1

if posicao == 0:
    print('Chapecoense não encontrado!')
else:
    print(f'Chapecoense na posição {posicao}º')

