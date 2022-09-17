times = ('Palmeiras', 'Internacional', 'Flamengo',
         'Fluminense', 'Corithias', 'Athletico-PR',
         'Atlético-MG', 'América-MG', 'Goiás',
         'Santos', 'Bragantino', 'Botafogo',
         'São Paulo', 'Ceará SC', 'Fortaleza',
         'Coritiba', 'Cuiabá', 'Avaí',
         'Atlético-GO', 'Juventude')
print('=-'*30)
print(f'Os times do Brasileirão: {times}')
print('=-'*30)
print(f'Os cinco primeiros: {times[0:5]}')
print('=-'*30)
print(f'Os quatros últimos são: {times[-4:]}')
print('=-'*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-'*30)
print(f'O Santos está na {times.index("Santos")+1} posição')

