nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota2+nota1)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media < 5.0:
    print('REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('RECUERAÇÃO!')
else:
    print('APROVADO')