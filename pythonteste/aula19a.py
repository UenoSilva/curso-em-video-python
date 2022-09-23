pessoas = {'nome': 'Gustavo', 'idade': 45}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas['nome'] = 'Leandro'
del pessoas['idade']
print(pessoas)

