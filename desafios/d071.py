cedula_50 = 0
cedula_20 = 0
cedula_10 = 0
cedula_01 = 0
print('='*30)
print('BANCO DO UENO'.center(30))
print('='*30)
while True:
    valor = int(input('Que valor você quer sacar? R$'))
    if valor >= 50:
        cedula_50 = valor // 50
        valor = valor - cedula_50 * 50
        print(f'Total de {cedula_50} de R$50')
    if valor >= 20:
        cedula_20 = valor // 20
        valor = valor - cedula_20 * 20
        print(f'Total de {cedula_20} de R$20')
    if valor >= 10:
        cedula_10 = valor // 10
        valor = valor - cedula_10 * 10
        print(f'Total de {cedula_10} de R$10')
    if valor >= 1:
        cedula_01 = valor // 1
        valor = valor - cedula_01 * 1
        print(f'Total de {cedula_01} de R$1')
    if valor == 0:
        break
print('='*30)
print('Volte sempre ao BANCO DO UENO! Tenha um bom dia!')